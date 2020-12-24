# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
from . import ctxf


def m_top(request):
    ctx = {}
    # if request.POST:
    #     power = request.
    return render(request, "m_top.html", ctx)


def m_department(request):
    ctx = {}
    # if request.POST:
    #     power = request.
    return render(request, "m_department.html", ctx)


def m_teacher(request):
    ctx = {}
    # if request.POST:
    #     power = request.
    return render(request, "m_teacher.html", ctx)


def m_student(request):
    ctx = {}
    # if request.POST:
    #     power = request.
    ctxf.getManage(ctx)
    return render(request, "m_student.html", ctx)


def m_apply(request):
    ctx = {}
    # if request.POST:
    #     power = request.
    ctxf.getManage(ctx)
    return render(request, "m_apply.html", ctx)


def m_drop_do(request):
    ctx = {}
    if request.POST:
        d = request.POST['did']
        d = Drop.objects.filter(pk=d).first()
        ctx['Sn'] = d.Sno.Sname
        ctx['Sno'] = d.Sno.Sno
        ctx['Dn'] = d.Sno.Dno.Dname
        ctx['reason'] = d.reason
        ctx['did'] = d.pk
    return render(request, "m_drop_do.html", ctx)


def m_change_do(request):
    ctx = {}
    if request.POST:
        c = request.POST['cid']
        c = Change.objects.filter(pk=c).first()
        ctx['Sn'] = c.Sno.Sname
        ctx['Sno'] = c.Sno.Sno
        ctx['Dn2'] = c.Dno.Dname
        ctx['Dn'] = c.Sno.Dno.Dname
        ctx['reason'] = c.reason
        ctx['cid'] = c.pk
    return render(request, "m_change_do.html", ctx)