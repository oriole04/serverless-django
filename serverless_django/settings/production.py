import os
from .base import *
from .installed import *

ALLOWED_HOSTS= ['windows-s3mqcan','www.ihm-chapel.com']
DEBUG=False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
print ("Using Production")

# Database 
HOME_PAGE_MSG = "Welcome to the Immaculate Heart of Mary Catholic Church, SSPX: "
BASIC_INFO_MSG = "Sunday Mass in Latin is at 6:30(Low Mass) and 9:00(High Mass) at the Acadamy, 777 221st Ave. Oak Grove; and Low Mass at 12:30 at the Chapel, 875 Manomen Ave. St. Paul"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
#        'NAME': 'C:/dev/serverless-django/db.sqlite3',

    }
}

#DATABASES = {
#    'default': {
#       'ENGINE': 'django.db.backends.postgresql',
#        'NAME': "production",
#        'USER': "dbproduser",
#        "PASSWORD": "biropa04",
#        "HOST": '127.0.0.1',
#        "PORT": 6543,
#    }
#}
STATIC_URL = '/static/'
# below taken from trydjango22/settings.py

LOCAL_STATIC_CDN_PATH = os.path.join(BASE_DIR, 'static_cdn_test')

STATIC_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, 'static')     # live cdn AWS S3
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

MEDIA_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, 'media')
MEDIA_URL = '/media/'       # django storages(setup for AWS instead of local one), etc. 
