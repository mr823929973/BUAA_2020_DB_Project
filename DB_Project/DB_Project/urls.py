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

from . import sth, login, sc, tc, manage, s_mux, t_mux, tutor, m_mux

urlpatterns = [
    url(r'^account/$', login.top),
    url(r'^login/$', login.login),
    url(r'^delete_c/$', sc.delete),
    url(r'^s_select/$', s_mux.s_select),
    url(r'^t_top/$', t_mux.t_top),
    url(r'^t_add/$', t_mux.t_add),
    url(r'^select_c/$', sc.select),
    url(r'^s_course/$', s_mux.s_course),
    url(r'^s_drop/$', s_mux.s_drop),
    url(r'^s_remark/$', s_mux.s_remark_top),
    url(r'^s_Dchange/$', s_mux.s_Dchange),
    url(r'^s_change_top/$', s_mux.s_change_top),
    url(r'^s_top/$', s_mux.s_top),
    url(r'^top/$', sth.top),
    url(r'^add_c/$', tc.add),
    url(r'^m_student/$', m_mux.m_student),
    url(r'^m_teacher/$', m_mux.m_teacher),
    url(r'^m_top/$', m_mux.m_top),
    url(r'^m_change_do/$', m_mux.m_change_do),
    url(r'^m_drop_do/$', m_mux.m_drop_do),
    url(r'^m_department/$', m_mux.m_department),
    url(r'^m_apply/$', m_mux.m_apply),
    url(r'^free_apply/$', sc.free_apply),
    url(r'^m_add_student/$', manage.m_add_student),
    url(r'^m_add_teacher/$', manage.m_add_teacher),
    url(r'^m_add_department/$', manage.m_add_department),
    url(r'^m_refresh/$', manage.m_refresh),
    url(r'^drop_out/$', manage.drop_out),
    url(r'^m_delete_all/$', manage.m_delete_all),
    url(r'^initial/$', manage.m_delete_all_t),
    url(r'^open_c/$', tc.open_c),
    url(r'^drop_apply/$', sc.drop_apply),
    url(r'^change_apply/$', sc.change_apply),
    url(r'^drop_solve/$', manage.drop_solve),
    url(r'^change_solve/$', manage.change_solve),
    url(r'^tc_lookHW/$', t_mux.tc_lookHW),
    url(r'^sc_doHW/$', s_mux.sc_doHW),
    url(r'^hw_solve/$', sc.hw_solve),
    url(r'^read_hw/$', t_mux.read_hw),
    url(r'^delete_hw/$', tc.delete_hw),
    url(r'^change_hw/$', t_mux.change_hw),
    url(r'^tc_free_do/$', t_mux.tc_free_do),
    url(r'^sc_lookHW/$', s_mux.sc_lookHW),
    url(r'^free_solve/$', tc.free_solve),
    url(r'^hw_read_do/$', tc.read_do),
    url(r'^tc_free/$', t_mux.tc_free),
    url(r'^tc_addHW/$', t_mux.tc_addHW),
    url(r'^tc_detail/$', t_mux.tc_detail),
    url(r'^sc_detail/$', s_mux.sc_detail),
    url(r'^hw_detail/$', t_mux.tc_hw_detail),
    url(r'^add_HW/$', tc.add_HW),
    url(r'^add_tutor/$', tutor.add_tutor),
    url(r'^tutor_before/$', tutor.tu_before),
    url(r'^delete_tutor/$', tutor.delete_tutor),
    url(r'^tuc_detail/$', t_mux.tuc_top),
    url(r'.*', sth.top),
]
