import pytest
from rest_framework.test import APIClient
from reservation.models import Rental, Reservation

pytestmark = pytest.mark.django_db
client = APIClient()

def test_create_reservation_validation(db):
  responseName = client.post('/reservation/', {'check_in': '2022-01-01', 'check_out': '2022-01-13'})
  responseDate = client.post('/reservation/', {'name': 'Rental 1', 'check_in': '2022-01', 'check_out': '2022-01-13'})

  assert responseName.status_code == 400
  assert responseName.json()['name'][0] == 'This field is required.'

  assert responseDate.status_code == 400
  assert responseDate.json()['check_in'][0] == 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.'

def test_create_reservation(db):
  response = client.post('/reservation/', {'name': 'Rental 1', 'check_in': '2022-01-12', 'check_out': '2022-01-15'})
  
  assert response.json()['detail'] == 'Reservation created'

def test_create_reservation(db):
  rental1 = Rental.objects.create(name='Rental 1')
  rental2 = Rental.objects.create(name='Rental 2')

  Reservation.objects.create(rental=rental1, check_in='2022-01-12', check_out='2022-01-15')
  Reservation.objects.create(rental=rental1, check_in='2021-12-12', check_out='2021-12-15')
  Reservation.objects.create(rental=rental1, check_in='2021-11-12', check_out='2021-11-15')

  Reservation.objects.create(rental=rental2, check_in='2022-01-12', check_out='2022-01-15')
  Reservation.objects.create(rental=rental2, check_in='2021-12-12', check_out='2021-12-15')

  response = client.get('/reservation', follow=True)

  sortedData = sorted(response.json(), key=lambda q: q['rental'])
  
  for index, data in enumerate(sortedData):
    if data['previous_reservation_id'] == None: continue
    assert data['previous_reservation_id'] == sortedData[index + 1]['id']
