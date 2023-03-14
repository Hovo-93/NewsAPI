#!/bin/bash
echo "Collect static files"
RUN python manage.py collectstatic --noinput
#Make database migrations
echo "Make database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

#Start server
echo "Start Server"
python manage.py runserver 0.0.0.0:8080