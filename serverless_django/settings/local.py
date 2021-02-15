import os
from .base import *
from .installed import *

HOME_PAGE_MSG = "Welcome to the Immaculate Heart of Mary Catholic Church, SSPX: "
BASIC_INFO_MSG = "Sunday Mass in Latin is at 6:30(Low Mass) and 9:00(High Mass) at the Acadamy, 777 221st Ave. Oak Grove; and Low Mass at 12:30 at the Chapel, 875 Manomen Ave. St. Paul"

print ("Using Local")

# Database 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
