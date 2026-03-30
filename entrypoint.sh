#!/bin/sh

if [ -n "$DB_NAME" ]
then
    echo "Waiting for database..."

    while ! nc -z $DB_HOST ${DB_PORT:-5432}; do
      sleep 0.1
    done

    echo "Database started"
fi

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

exec "$@"
