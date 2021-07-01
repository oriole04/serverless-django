"""serverless_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from pages import views as pages_views
from pages.views import (example_page, home_page, about_page, contact_page)
from blog.views import (
    blog_post_create_view
)
#    path('', home_view),
#    path('admin/', admin.site.urls),
#]
urlpatterns = [
    path('', home_page),
    path('blog-new/', blog_post_create_view),  #go to blog-new/ before blog/
    path('blog/', include('blog.urls')),
    path('about/', about_page),
    path('contact/', contact_page),
    path('example/', example_page),
    path('admin/', admin.site.urls),    # by having a .urls file inside of it, its pluggable!
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

