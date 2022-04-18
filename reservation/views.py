from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from reservation.models import Reservation
from reservation.serializers import RentalSerializer, ReservationSerializer
from reservation.service import get_reservations

class ReservationList(APIView):
  # list all reservations
  def get(self, request):
    reservations = get_reservations()
    serializer = ReservationSerializer(reservations, many=True)
    
    return Response(data=serializer.data, status=status.HTTP_200_OK)
  
  # create a new reservation
  def post(self, request):
    rental_serializer = RentalSerializer(data=request.data)

    if rental_serializer.is_valid():
      reservation_serializer = ReservationSerializer(data=request.data)

      if reservation_serializer.is_valid():
        rental, _ = rental_serializer.save()
        reservation_serializer.save(rental=rental)

        return Response(data={'detail': 'Reservation created'}, status=status.HTTP_201_CREATED)
      
      return Response(data=reservation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(data=rental_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
