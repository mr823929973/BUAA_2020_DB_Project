"""DB_Project URL Configuration

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
from django.urls import path
from django.conf.urls import url

from . import sth, login, sc, tc

urlpatterns = [
    url(r'^account/$', login.top),
    url(r'^login/$', login.login),
    url(r'^delete_c/$', sc.delete),
    url(r'^select_c/$', sc.select),
    url(r'^top/$', sth.top),
    url(r'^add_c/$', tc.add),
    url(r'^open_c/$', tc.open_c),
    url(r'.*', sth.top),
]
