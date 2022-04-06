from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reservation.models import Reservation
from reservation.serializers import RentalSerializer, ReservationSerializer

class ReservationList(APIView):
  # list all reservations
  def get(self, request, format=None):
    data = []
    
    rentals = []
    previous_reservation_id = None

    reservations = Reservation.objects.prefetch_related('rental').all()
    
    for reservation in reservations:
      if reservation.rental.name not in rentals:
        previous_reservation_id = None
        rentals.append(reservation.rental.name)

      _data = {
        'id': reservation.id,
        'rental_name': reservation.rental.name,
        'check_in': reservation.check_in,
        'check_out': reservation.check_out,
        'previous_reservation_id': previous_reservation_id
      }

      previous_reservation_id = reservation.id

      data.append(_data)
    
    return Response(data)
  
  # create a new reservation
  def post(self, request, format=None):
    rental_serializer = RentalSerializer(data=request.data)

    if rental_serializer.is_valid():
      reservation_serializer = ReservationSerializer(data=request.data)

      if reservation_serializer.is_valid():
        rental, _ = rental_serializer.save()
        reservation_serializer.save(rental = rental)
        
        return Response(reservation_serializer.data, status=status.HTTP_201_CREATED)
      
      return Response(reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(rental_serializer.errors, status.HTTP_400_BAD_REQUEST)
