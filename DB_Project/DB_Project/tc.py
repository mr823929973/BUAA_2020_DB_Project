# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
from . import ctxf


def add(request):
    ctx = {}
    if request.POST:
        Cname = request.POST['Cname']
        credit = request.POST['credit']
        t = request.POST['user']
        t = Teacher.objects.filter(Tno=t).first()
        v = request.POST['v']
        if len(Course.objects.filter(Cname=Cname)) != 0:
            ctx['m1'] = '已有同名课程，增加失败！'
        else:
            Course.objects.create(Cname=Cname, credit=credit, v=v, Cno=getCno())
            ctx['m1'] = '成功增加课程！'
        ctxf.getTinfo(t, ctx)
    return render(request, "t_add.html", ctx)


def open_c(request):
    ctx = {}
    if request.POST:
        Cno = request.POST['Cno']
        c = Course.objects.filter(Cno=Cno).first()
        Dno = request.POST['Dno']
        d = Department.objects.filter(Dno=Dno).first()
        t = request.POST['user']
        t = Teacher.objects.filter(Tno=t).first()

        if len(TC.objects.filter(Cno=Cno, Dno=Dno, Tno=t.Tno)) != 0:
            ctx['m1'] = '已经在该院系开设过相同课程，开课失败！'
        else:
            TC.objects.create(Cno=c, Dno=d, Tno=t)
            ctx['m1'] = '成功开设课程！'
        ctxf.getTinfo(t, ctx)
    return render(request, "t_add.html", ctx)


def add_HW(request):
    ctx = {}
    if request.POST:
        name = request.POST['name']
        question = request.POST['question']
        ift = request.POST.getlist('ift')
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()

        conflict = HW.objects.filter(name=name, TC=tc)

        if len(conflict) != 0:
            ctx['m1'] = '课内已有同名作业！'
            ctxf.getTCinfo(tc, ctx)
            return render(request, "tc_addHW.html", ctx)
        else:
            if 'yes' in ift:
                times = request.POST['times']
                HW.objects.create(name=name, question=question, times=times, TC=tc)
            else:
                HW.objects.create(name=name, question=question, times=0, TC=tc)
            ctx['m1'] = '成功发布作业！'
        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_lookHW.html", ctx)
