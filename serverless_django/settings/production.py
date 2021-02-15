import os
from .base import *
from .installed import *

ALLOWED_HOSTS= ['serverless-django-i4oprjwhka-uc.a.run.app','www.ihm-chapel.com']
DEBUG=False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", ')w4^6y$l=c3fk9ag!&t5=__xw1+%+j00c)lfw8gmq+fg3&%2#h')

print ("Using Production")
# Database 
HOME_PAGE_MSG = "Welcome to the Immaculate Heart of Mary Catholic Church, SSPX: "
BASIC_INFO_MSG = "Sunday Mass in Latin is at 6:30(Low Mass) and 9:00(High Mass) at the Acadamy, 777 221st Ave. Oak Grove; and Low Mass at 12:30 at the Chapel, 875 Manomen Ave. St. Paul"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
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
