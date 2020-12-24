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
        who = request.POST['who']
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, tc, ctx)
            return render(request, "tuc_addHW.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_addHW.html", ctx)


def tc_lookHW(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        who = request.POST['who']
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, tc, ctx)
            return render(request, "tuc_lookHW.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_lookHW.html", ctx)


def tc_hw_detail(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        hw = request.POST['hw']
        hw = HW.objects.filter(pk=hw).first()
        ctxf.getTCHWinfo(ctx, tc, hw)
        who = request.POST['who']
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, tc, ctx)
            return render(request, "tuc_hw_detail.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_hw_detail.html", ctx)


def change_hw(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        hw = request.POST['hw']
        hw = HW.objects.filter(pk=hw).first()
        who = request.POST['who']
        ctx['hw'] = hw
        ctx['hwid'] = hw.pk
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, tc, ctx)
            return render(request, "tuc_hw_change.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_hw_change.html", ctx)


def read_hw(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        hw = request.POST['hw']
        hw = HW.objects.filter(pk=hw).first()
        s = request.POST['Sno']
        s = Student.objects.filter(pk=s).first()
        ctx['hw'] = hw
        ctx['hwid'] = hw.pk
        hwd = HWD.objects.filter(HW=hw, Sno=s).first()
        if hwd.read:
            ctx['back'] = hwd.back
            ctx['point'] = hwd.point
        else:
            ctx['back'] = ''
        ctx['hwd'] = hwd
        who = request.POST['who']
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, tc, ctx)
            return render(request, "tuc_read_hw.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_read_hw.html", ctx)


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


def tuc_top(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        s = request.POST['TUno']
        s = Student.objects.filter(pk=s).first()
        ctxf.getTCinfo(tc, ctx)
        ctxf.getSinfo(s, ctx)
    return render(request, "tuc_top.html", ctx)