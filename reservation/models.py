from django.db import models

class Reservation(models.Model):
  rental_name = models.CharField(max_length=40)
  check_in = models.DateField()
  check_out = models.DateField()
  previous_reservation_id = models.BigIntegerField(blank=True, null=True)
