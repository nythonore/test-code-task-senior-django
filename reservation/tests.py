import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db
client = APIClient()

def test_create_reservation_validation(db):
  responseName = client.post('/reservation/', {'check_in': '2022-01-01', 'check_out': '2022-01-13'})
  responseDate = client.post('/reservation/', {'name': 'Rental 1', 'check_in': '2022-01', 'check_out': '2022-01-13'})

  assert responseName.status_code == 400
  assert responseName.json()['name'][0] == 'This field is required.'

  assert responseDate.status_code == 400
  assert responseDate.json()['check_in'][0] == 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.'

def test_reservation(db):
  # add data chronologically
  client.post('/reservation/', {'rental_name': 'Rental 1', 'check_in': '2022-01-01', 'check_out': '2022-01-13'})
  client.post('/reservation/', {'rental_name': 'Rental 2', 'check_in': '2022-01-02', 'check_out': '2022-01-20'})
  client.post('/reservation/', {'rental_name': 'Rental 1', 'check_in': '2022-01-20', 'check_out': '2022-02-10'})
  client.post('/reservation/', {'rental_name': 'Rental 2', 'check_in': '2022-01-20', 'check_out': '2022-02-11'})
  client.post('/reservation/', {'rental_name': 'Rental 1', 'check_in': '2022-02-20', 'check_out': '2022-03-10'})

  response = client.get('/reservation', follow=True)

  rentals = []
  previous_reservation_id = None

  for reservation in response.json():
    if reservation['rental_name'] not in rentals:
      previous_reservation_id = None
      rentals.append(reservation['rental_name'])
    
    assert previous_reservation_id == reservation['previous_reservation_id']

    previous_reservation_id = reservation['id']
