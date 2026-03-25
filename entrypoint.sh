#!/bin/sh

if [ "$DB_NAME" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

exec "$@"
