"""photography URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from crm import views
from django.conf.urls.static import static
from django.conf import settings
from photoexp.views import *
from about.views import about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page, name='index'),
    path('thanks/', views.thanks_page, name='thanks_page'),
    path('<int:pk>', PhototDetail.as_view(), name='photo_detail'),
    path('about', about_page, name='about' )
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
