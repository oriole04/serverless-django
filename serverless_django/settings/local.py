import os
from serverless_django.settings.production import STATIC_ROOT
from .base import *
from .installed import *

ALLOWED_HOSTS = ['windows-s3mqcan',
    '127.0.0.1', 'localhost', 'kubernetes.docker.internal'
    ]
HOME_PAGE_MSG = "Welcome to the Immaculate Heart of Mary Catholic Church, SSPX: "
BASIC_INFO_MSG = "Sunday Mass in Latin is at 6:30(Low Mass) and 9:00(High Mass) at the Acadamy, 777 221st Ave. Oak Grove; and Low Mass at 12:30 at the Chapel, 875 Manomen Ave. St. Paul"
DJANGO_SETTINGS_MODULE = 'serverless_django.settings.local' 

print ("Using Local with STATIC_ROOT='/static/'")

# Database 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
#        'NAME': 'C:/dev/serverless-django/db.sqlite3',

    }
}
# Database 
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': "local",
#        'USER': "dblocaluser",
#        "PASSWORD": "biropa04",
#        "HOST": '127.0.0.1',
#        "PORT": 5432,
#    }
#}
STATIC_URL = '/static/'
# below taken from trydjango22/settings.py

#LOCAL_STATIC_CDN_PATH = os.path.join(os.path.dirname(BASE_DIR), 'serverless-django\static_cdn_test')
LOCAL_STATIC_CDN_PATH = os.path.join(BASE_DIR, 'static_cdn_test')

#STATIC_ROOT = 'C:\dev\serverless-django\static'
#STATIC_ROOT = os.path.join(BASE_DIR, '\static')     # live cdn AWS S3
#STATIC_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, '\static')     # live cdn AWS S3
#STATIC_ROOT = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

MEDIA_ROOT = os.path.join(LOCAL_STATIC_CDN_PATH, 'media')
MEDIA_URL = '/media/'       # django storages(setup for AWS instead of local one), etc. 
print (DJANGO_SETTINGS_MODULE, STATIC_ROOT, BASE_DIR, LOCAL_STATIC_CDN_PATH, STATIC_URL, MEDIA_ROOT, MEDIA_URL)

