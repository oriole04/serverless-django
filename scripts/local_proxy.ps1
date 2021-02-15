$env:DJANGO_SETTINGS_MODULE="serverless_django.settings.local_proxy"
waitress-serve serverless_django.wsgi:application
