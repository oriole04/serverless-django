import os
from .base import *
from .installed import *

HOME_PAGE_MSG = "Welcome to the Immaculate Heart of Mary SSPX, Saint Paul Chapel: Local Proxy Site under construction"
BASIC_INFO_MSG = "Mass for Sunday is at 7:00, 9:00(High Mass) and 11:00"

print ("Using Local Proxy")
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
