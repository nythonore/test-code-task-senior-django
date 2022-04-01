# Test Code Task - Senior Django

#### Deliverables

```
Add the view with the table of Reservations with "previous reservation ID".
Previous reservation is a reservation that is before the current one into same
rental.

Also, add a tests.
Create it into github repo and provide a link to it.
```

#### Prerequisites

Make sure you have already installed [Python 3.7+](https://www.python.org), [Pip](https://pip.pypa.io/en/stable/installation) and [PostgreSQL](https://www.postgresql.org/).

#### Installing

```
$ git clone https://github.com/nythonore/test-code-task-senior-django
$ cd test-code-task-senior-django
$ pip install psycopg2
$ pip install -r requirements.txt
```

Create .env File in project directory root

```
SECRET_KEY=secret
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=dbname
DB_USERNAME=user
DB_PASSWORD=password
```

Run DB Migration

```
$ python manage.py migrate
```

#### Start

```
$ python manage.py runserver
```

Go to [http://localhost:8000/reservation/](http://localhost:8000/reservation/)

#### Available Endpoint

```
GET - http://localhost:8000/reservation/ (List All Reservations)
```

```
POST - http://localhost:8000/reservation/ (Create a Reservation)
{
    "rental_name": "Rental 1",
    "check_in": "2000-01-01",
    "check_out": "2000-01-01"
}
```

#### Testing

```
$ pytest
```
