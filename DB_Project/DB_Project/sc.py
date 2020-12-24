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
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc)
        s = request.POST['s']
        s = Student.objects.filter(Sno=s).first()
        if len(sc) == 0:
            ctx['m1'] = '该学生没有选择该课，无法退课！'
        else:
            sc.delete()
            ctx['m1'] = '退课成功！'
        ctxf.getSinfo(s, ctx)
    return render(request, "s_course.html", ctx)


def free_apply(request):
    ctx = {}
    if request.POST:
        sc = request.POST['sc']
        reason = request.POST['reason']

        sc = SC.objects.filter(pk=sc).first()

        conflict = FreeApply.objects.filter(SC=sc)

        if len(conflict) != 0:
            ctx['m1'] = '已经申请过了，不能重复申请！'
        else:
            FreeApply.objects.create(SC=sc, reason=reason)
            ctx['m1'] = '免修申请已提交！'
        ctxf.getSCinfo(sc, ctx)
    return render(request, "sc_top.html", ctx)


def hw_solve(request):
    ctx = {}
    if request.POST:
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        content = request.POST['content']
        s = sc.Sno
        hw = request.POST['hw']
        hw = HW.objects.filter(pk=hw).first()

        had = HWD.objects.filter(HW=hw, Sno=s)

        if len(had) != 0:
            had = had.first()
            if had.had >= hw.times:
                ctx['m1'] = '已达提交次数上限！'
            else:
                had.had = had.had + 1
                had.content = content
                had.save()
                ctx['m1'] = '作业修改成功！'
        else:
            HWD.objects.create(Sno=s, HW=hw, content=content, had=1)
            ctx['m1'] = '作业已提交！'
        ctxf.getSCinfo(sc, ctx)
    return render(request, "sc_lookHW.html", ctx)


def drop_apply(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        reason = request.POST['reason']

        s = Student.objects.filter(pk=s).first()

        conflict = Drop.objects.filter(Sno=s, read=False)

        if len(conflict) != 0:
            ctx['m1'] = '上一次审批还在进行，请勿重复提交！'
        else:
            Drop.objects.create(Sno=s, reason=reason)
            ctx['m1'] = '退学申请已提交！'
        ctxf.getSinfo(s, ctx)
    return render(request, "s_top.html", ctx)


def change_apply(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        reason = request.POST['reason']
        d = request.POST['Dno']
        d = Department.objects.filter(pk=d).first()
        s = Student.objects.filter(pk=s).first()

        conflict = Change.objects.filter(Sno=s, read=False)
        cs = SC.objects.filter(Sno=s, end=False)

        if len(conflict) != 0:
            ctx['m1'] = '上一次审批还在进行，请勿重复申请！'
        elif len(cs) != 0:
            ctx['m1'] = '还有尚未结课的本系课程，请结课后再进行申请！'
        else:
            Change.objects.create(Sno=s, Dno=d, reason=reason)
            ctx['m1'] = '转系申请已提交！'
        ctxf.getSinfo(s, ctx)
    return render(request, "s_top.html", ctx)
