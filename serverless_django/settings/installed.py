INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'  # in app directory for templates will pick up app's .html file!
    # also put into urls file for apps (point to include blog/urls file path)
]