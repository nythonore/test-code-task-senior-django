import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db
client = APIClient()  

def test_list_reservations(db, reservation_factory):
  for i in range(10):
    reservation_factory(rental_name=f'Rental {i}')
  
  response = client.get('/reservation', follow=True)

  assert len(response.json()) == 10

def test_create_reservation(db):
  key = 'previous_reservation_id'
  data = {'check_in': '2022-01-01', 'check_out': '2022-01-01'}
  
  response1 = client.post('/reservation/', {**data, 'rental_name': 'Rental 1'})
  response2 = client.post('/reservation/', {**data, 'rental_name': 'Rental 1'})
  response3 = client.post('/reservation/', {**data, 'rental_name': 'Rental 1'})

  response4 = client.post('/reservation/', {**data, 'rental_name': 'Rental 2'})
  response5 = client.post('/reservation/', {**data, 'rental_name': 'Rental 2'})

  assert response1.json()[key] == None
  assert response2.json()[key] == response1.json()['id']
  assert response3.json()[key] == response2.json()['id']

  assert response4.json()[key] == None
  assert response5.json()[key] == response4.json()['id']
