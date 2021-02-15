$env:DJANGO_SETTINGS_MODULE="serverless_django.settings.local_proxy"
python manage.py migrate
$env:DJANGO_SETTINGS_MODULE="serverless_django.settings.production"
python manage.py migrate
