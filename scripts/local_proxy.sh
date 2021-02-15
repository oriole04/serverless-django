DJANGO_SETTINGS_MODULE=serverless_django.settings.local_proxy waitress-serve serverless_django.wsgi:application 
#DJANGO_SETTINGS_MODULE=serverless_django.settings.local_proxy
#gunicorn       serverless_django.wsgi:application --env DJANGO_SETTINGS_MODULE=serverless_django.settings.local_proxy 