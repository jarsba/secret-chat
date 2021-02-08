#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $SC_DB_URL $SC_DB_PORT; do
  echo "Waiting for postgres..."
  sleep 3
done

echo "PostgreSQL started"

FLASK_APP=main.py flask run --host 0.0.0.0

exec "$@"