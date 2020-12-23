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

