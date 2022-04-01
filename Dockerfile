FROM python:3.8-slim

RUN apt-get update
RUN apt-get -y install libpq-dev gcc

# Working directory
WORKDIR /app

# Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy Requirements
COPY Pipfile .
COPY Pipfile.lock .

# Upgrade PIP
RUN set -ex && pip install --upgrade pip

# Install Required Dependecire
RUN set -ex && pip install pipenv psycopg2 --upgrade

# Install Requirements
RUN set -ex && pipenv lock -r > requirements.txt
RUN set -ex && pip install -r requirements.txt

# Copy App
COPY . .

# Expose Port App
EXPOSE 4000

# Start App
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
