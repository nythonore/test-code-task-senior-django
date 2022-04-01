from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reservation.models import Reservation
from reservation.serializers import ReservationSerializer

class ReservationList(APIView):
  # list all reservations
  def get(self, request, format=None):
    # query all reservations in order
    reservations = Reservation.objects.order_by('rental_name', 'id')
    serializer = ReservationSerializer(reservations, many=True)
    
    return Response(serializer.data)
  
  # create a new reservation
  def post(self, request, format=None):
    serializer = ReservationSerializer(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
