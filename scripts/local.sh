#$env:DJANGO_SETTINGS_MODULE="serverless_django.settings.local"

#waitress-serve serverless_django.wsgi:application
#waitress.serve(serverless_django.wsgi.application) # need to import serverless_django.wsgi first before calling this.
DJANGO_SETTINGS_MODULE=serverless_django.settings.local waitress-serve serverless_django.wsgi:application 
