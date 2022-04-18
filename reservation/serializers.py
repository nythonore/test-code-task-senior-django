from rest_framework import serializers
from reservation.models import Rental, Reservation 

class RentalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rental
    fields = ['name']
  
  def create(self, data):
    return Rental.objects.get_or_create(**data)

class ReservationSerializer(serializers.ModelSerializer):
  rental = serializers.SerializerMethodField()
  previous_reservation_id = serializers.SerializerMethodField()

  def get_rental(self, obj):
    return obj.rental.name

  def get_previous_reservation_id(self, obj):
    return obj.previous_reservation_id

  class Meta:
    model = Reservation
    fields = ['id', 'rental', 'check_in', 'check_out', 'previous_reservation_id']
