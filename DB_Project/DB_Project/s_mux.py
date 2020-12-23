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

# 接收POST请求数据
def delete(request):
    ctx = {}
    if request.POST:
        s = request.POST['user']
        c = request.POST['course']
        s = Student.objects.filter(Sno=s).first()
        sc = SC.objects.filter(Sno=s.Sno, Cno=c)
        if len(sc) == 0:
            ctx['m1'] = '该学生没有选择该课，无法退课！'
        else:
            sc.delete()
            ctx['m1'] = '退课成功！'
        ctxf.getSinfo(s, ctx)
    return render(request, "top.html", ctx)
