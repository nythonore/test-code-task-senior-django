from django.db import models

class Rental(models.Model):
  name = models.CharField(max_length=40)

class Reservation(models.Model):
  check_in = models.DateField()
  check_out = models.DateField()
  rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='rental')

  class Meta:
    ordering = ['id']
