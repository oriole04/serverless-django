DJANGO_SETTINGS_MODULE=serverless_django.settings.local_proxy python manage.py migrate
DJANGO_SETTINGS_MODULE=serverless_django.settings.production python manage.py migrate
#you have to start the proxy server on host 127.0.0.1 and port 6543 before running this. See db_proxy.sh
