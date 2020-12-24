# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
from . import ctxf


def t_top(request):
    ctx = {}
    if request.POST:
        t = request.POST['Tno']
        t = Teacher.objects.filter(Tno=t).first()
        ctxf.getTinfo(t, ctx)
    return render(request, "t_top.html", ctx)


def tc_detail(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_top.html", ctx)


def tc_free_do(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        ctxf.getTCinfo(tc, ctx)
        pk = request.POST['apply']
        pk = FreeApply.objects.filter(pk=pk).first()
        ctx['reason'] = pk.reason
        ctx['scid'] = pk.SC.pk
        ctx['freeid'] = pk.pk
        ctx['S'] = pk.SC.Sno
    return render(request, "tc_free_do.html", ctx)


def tc_addHW(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_addHW.html", ctx)


def tc_lookHW(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_lookHW.html", ctx)


def tc_hw_detail(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        hw = request.POST['hw']
        hw = HW.objects.filter(pk=hw).first()
        ctxf.getTCinfo(tc, ctx)
        ctx['hw'] = hw
        hwds = HWD.objects.filter(HW=hw)
        ctx['done'] = hwds.count()

        scs = SC.objects.filter(TC=tc)
        s_hw_list = []
        for i in scs:
            one = {}
            one['Sn'] = i.Sno.Sname
            hwd_now = hwds.filter(Sno=i.Sno)
            if len(hwd_now) == 0:
                one['had_time'] = 0
            else:
                hwd_now = hwd_now.first()
                one['had_time'] = hwd_now.had
                one['read'] = hwd_now.read
                one['point'] = hwd_now.point
            s_hw_list.append(one)
        ctx['s_hw_list'] = s_hw_list
    return render(request, "tc_hw_detail.html", ctx)


def change_hw(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        hw = request.POST['hw']
        hw = HW.objects.filter(pk=hw).first()
        ctxf.getTCinfo(tc, ctx)
        ctx['hw'] = hw
        ctx['hwid'] = hw.pk
    return render(request, "tc_hw_change.html", ctx)


def tc_free(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_free.html", ctx)


def t_add(request):
    ctx = {}
    if request.POST:
        t = request.POST['Tno']
        t = Teacher.objects.filter(Tno=t).first()
        ctxf.getTinfo(t, ctx)
    return render(request, "t_add.html", ctx)

