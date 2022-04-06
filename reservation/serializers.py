from rest_framework import serializers
from reservation.models import Rental, Reservation 

class RentalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rental
    fields = ['name']
  
  def create(self, data):
    return Rental.objects.get_or_create(**data)

class ReservationSerializer(serializers.ModelSerializer):
  rental = RentalSerializer(read_only=True)

  class Meta:
    model = Reservation
    fields = ['id', 'rental', 'check_in', 'check_out']
  
  def create(self, data):
    return Reservation.objects.create(**data)
