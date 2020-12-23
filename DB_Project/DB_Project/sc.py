# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse

from . import ctxf


def select(request):
    ctx = {}
    if request.POST:
        s = request.POST['user']
        t = request.POST['tc']
        t = TC.objects.filter(pk=t).first()
        s = Student.objects.filter(Sno=s).first()
        sc = SC.objects.filter(Sno=s.Sno, Cno=t.Cno)
        al = SC.objects.filter(TC=t).count()

        if len(sc) != 0:
            ctx['m1'] = '该学生已选择过同名的课，不能重复选课！'
        elif t.Dno != s.Dno:
            ctx['m1'] = '只能选择本系开设的课程！'
        elif t.Cno.v <= al:
            ctx['m1'] = '人数已满，选课失败！'
        else:
            SC.objects.create(Sno=s, Cno=t.Cno, TC=t)
            ctx['m1'] = '选课成功！'
        ctxf.getSinfo(s, ctx)
    return render(request, "s_select.html", ctx)


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
    return render(request, "s_course.html", ctx)
