"""djangoProject URL Configuration

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
from django.urls import path

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from core.views import render_glavnoi, render_katalog, render_uslugi, render_calc, render_about, render_faq, render_contacts
from djangoProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('katalog', render_katalog),
    path('uslugi', render_uslugi),
    path('calc', render_calc),
    path('about', render_about),
    path('faq', render_faq),
    path('contacts', render_contacts),
    path('', render_glavnoi),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
