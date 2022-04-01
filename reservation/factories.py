import factory
from reservation.models import Reservation

class ReservationFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Reservation

  check_in = '2022-01-01'
  check_out = '2022-01-01'
