import os
from .base import *
from .installed import *
from decouple import config
from serverless_django.settings.production import STATIC_ROOT

HOME_PAGE_MSG = "Welcome to the Immaculate Heart of Mary SSPX, Saint Paul Chapel: Local Proxy Site under construction"
BASIC_INFO_MSG = "Mass for Sunday is at 7:00, 9:00(High Mass) and 11:00"

print ("Using Local Proxy")
ALLOWED_HOSTS= ['windows-s3mqcan','127.0.0.1', 'localhost']

DJANGO_SETTINGS_MODULE = 'serverless_django.settings.local_proxy' 

# Database 
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': "local",
#        'USER': "dblocaluser",
#        "PASSWORD": "biropa04",
#        "HOST": '127.0.0.1',
#        "PORT": 6543,
#    }
#}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
#        'NAME' : [os.path.join(BASE_DIR, '/db.sqlite3')],
#        'NAME' : os.path.join(os.path.dirname(BASE_DIR), 'serverless-django\db.sqlite3'),
#        'NAME': 'BASE_DIR / db_local_proxy',
        'NAME': 'db_local_proxy',
        'USER': 'oriole04',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        "PORT": 3306,       # 3306
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

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
print (DB_PASSWORD, DJANGO_SETTINGS_MODULE, STATIC_ROOT, BASE_DIR, LOCAL_STATIC_CDN_PATH, STATIC_URL, MEDIA_ROOT, MEDIA_URL)
