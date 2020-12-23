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

from . import sth, login, sc, tc, manage, s_mux, t_mux

urlpatterns = [
    url(r'^account/$', login.top),
    url(r'^login/$', login.login),
    url(r'^delete_c/$', sc.delete),
    url(r'^s_select/$', s_mux.s_select),
    url(r'^t_top/$', t_mux.t_top),
    url(r'^t_add/$', t_mux.t_add),
    url(r'^select_c/$', sc.select),
    url(r'^s_course/$', s_mux.s_course),
    url(r'^top/$', sth.top),
    url(r'^add_c/$', tc.add),
    url(r'^m_add_student/$', manage.m_add_student),
    url(r'^m_add_teacher/$', manage.m_add_teacher),
    url(r'^m_add_department/$', manage.m_add_department),
    url(r'^m_refresh/$', manage.m_refresh),
    url(r'^m_delete_all/$', manage.m_delete_all),
    url(r'^open_c/$', tc.open_c),
    url(r'.*', sth.top),
]
