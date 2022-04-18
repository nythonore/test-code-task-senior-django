from django.db.models import OuterRef, Subquery
from reservation.models import Reservation

def get_reservations():
  subquery = Reservation.objects.filter(
    check_out__lte = OuterRef('check_in'),
    rental_id = OuterRef('rental_id')
  )

  return Reservation.objects.select_related('rental').annotate(
    previous_reservation_id = Subquery(subquery.values('id')[:1])
  ).all()
