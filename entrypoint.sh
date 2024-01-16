#!/bin/sh

# python manage.py flush --no-input
pip install -r requirements.txt
exec "$@"