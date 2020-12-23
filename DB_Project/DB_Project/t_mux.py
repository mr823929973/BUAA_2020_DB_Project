# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
import random


def getCno():
    i = random.randint(0, 100000)
    while len(Course.objects.filter(Cno=i)) != 0:
        i = random.randint(0, 100000)
    return i


def getTinfo(t, ctx):
    tc = TC.objects.filter(Tno=t.Tno)
    tc_list = []
    for i in tc:
        one = {}
        one['Cno'] = i.Cno.Cno
        one['Tn'] = i.Tno.Tname
        one['Tno'] = i.Tno.Tno
        one['Cn'] = i.Cno.Cname
        one['Dno'] = i.Dno.Dno
        one['Dn'] = i.Dno.Dname
        one['credit'] = i.Cno.credit
        one['tid'] = i.pk
        one['v'] = i.Cno.v
        one['s'] = SC.objects.filter(TC=i.pk).count()
        tc_list.append(one)

    ctx['tc_list'] = tc_list
    ctx['d_list'] = Department.objects.all()
    ctx['cs_list'] = Course.objects.all()
    ctx['t'] = 'teacher'
    ctx['user'] = t


def t_top(request):
    ctx = {}
    if request.POST:
        t = request.POST['Tno']
        t = Teacher.objects.filter(Tno=t).first()
        getTinfo(t, ctx)
    return render(request, "t_top.html", ctx)


def t_add(request):
    ctx = {}
    if request.POST:
        t = request.POST['Tno']
        t = Teacher.objects.filter(Tno=t).first()
        getTinfo(t, ctx)
    return render(request, "t_add.html", ctx)