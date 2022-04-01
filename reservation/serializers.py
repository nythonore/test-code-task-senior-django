from rest_framework import serializers
from reservation.models import Reservation 

class ReservationSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  rental_name = serializers.CharField(required=True, max_length=40)
  check_in = serializers.DateField(required=True)
  check_out = serializers.DateField(required=True)
  previous_reservation_id = serializers.IntegerField(required=False, allow_null=True)

  def create(self, data):
    try:
      last_rental = Reservation.objects.filter(rental_name=data['rental_name']).latest('id')
    except Reservation.DoesNotExist:
      last_rental = None
    
    if last_rental: data['previous_reservation_id'] = last_rental.id

    return Reservation.objects.create(**data)
