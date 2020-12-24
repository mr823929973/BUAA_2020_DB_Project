# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse

from . import ctxf


def s_select(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        ctxf.getSinfo(s, ctx)
    return render(request, "s_select.html", ctx)


def s_course(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        ctxf.getSinfo(s, ctx)
    return render(request, "s_course.html", ctx)


def sc_detail(request):
    ctx = {}
    if request.POST:
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        ctxf.getSCinfo(sc, ctx)
    return render(request, "sc_top.html", ctx)


def sc_lookHW(request):
    ctx = {}
    if request.POST:
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        ctxf.getSCinfo(sc, ctx)
    return render(request, "sc_lookHW.html", ctx)


def sc_doHW(request):
    ctx = {}
    if request.POST:
        hw = request.POST['hwid']
        hw = HW.objects.filter(pk=hw)
        s = request.POST['Sno']
        s = Student.objects.filter(pk=s).first()
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        ctxf.getSCinfo(sc, ctx)

        if len(hw) == 0:
            ctx['m1'] = '作业不存在！'
            return render(request, "sc_lookHW.html", ctx)
        hw = hw.first()

        ctx['hw'] = hw
        hwd = HWD.objects.filter(HW=hw, Sno=s)
        if len(hwd) == 0:
            ctx['hwd_read'] = False
            ctx['had_time'] = 0
            ctx['hw_content'] = ''
        else:
            ctx['hwd_read'] = hwd.first().read
            ctx['hwd'] = hwd
            ctx['had_time'] = hwd.first().had
            ctx['hw_content'] = hwd.first().content
    return render(request, "sc_HW_do.html", ctx)