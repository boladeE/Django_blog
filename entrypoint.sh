#!/usr/bin/env bash
ls
cd blog_project
ls
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn blog_project.wsgi -b 0.0.0.0:8000
