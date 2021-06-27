import os
from .base import *
from .installed import *

ALLOWED_HOSTS= ['windows-s3mqcan','www.ihm-chapel.com']
DEBUG=False
DJANGO_SETTINGS_MODULE = 'serverless_django.settings.production' 

print ("Using Production")

# Database 
HOME_PAGE_MSG = "Welcome to the Immaculate Heart of Mary Catholic Church, SSPX: "
BASIC_INFO_MSG = "Sunday Mass in Latin is at 6:30(Low Mass) and 9:00(High Mass) at the Acadamy, 777 221st Ave. Oak Grove; and Low Mass at 12:30 at the Chapel, 875 Manomen Ave. St. Paul"

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
##        'NAME': 'C:/dev/serverless-django/db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oriole04$db1',
        'USER': 'oriole04',
        'PASSWORD': DB_PASSWORD,  #DB_PASSWORD this may need to change!
        'HOST': 'oriole04.mysql.pythonanywhere-services.com',
        "PORT": 3306,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

STATIC_URL = '/static/'
# below taken from trydjango22/settings.py

LOCAL_STATIC_CDN_PATH = os.path.join(BASE_DIR, 'static_cdn_test')

STATIC_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, 'static')     # live cdn AWS S3
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

MEDIA_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, 'media')
MEDIA_URL = '/media/'       # django storages(setup for AWS instead of local one), etc. 
