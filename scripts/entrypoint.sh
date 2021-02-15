#! /bin/bash

DJANGO_SETTINGS_MODULE=serverless_django.settings.local waitress-serve --listen=0.0.0.0:$PORT serverless_django.wsgi:application 

# DJANGO_SETTINGS_MODULE=serverless_django.settings.local uvicorn serverless_django.wsgi:application --host 0.0.0.0 --port 8888  GETS SERVER ERROR
