#!/usr/bin/env bash

cd blog_project
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn blog_project.wsgi -b 0.0.0.0:8000
