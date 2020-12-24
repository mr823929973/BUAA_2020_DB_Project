# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
from . import ctxf
import random


def getCno():
    i = random.randint(0, 100000)
    while len(Course.objects.filter(Cno=i)) != 0:
        i = random.randint(0, 100000)
    return i


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
        doing = request.POST['hw_type']

        conflict = HW.objects.filter(name=name, TC=tc)

        if len(conflict) != 0 and doing == 'add':
            ctx['m1'] = '课内已有同名作业！'
            who = request.POST['who']
            if who == 'tutor':
                tu = request.POST['TUno']
                tu = Student.objects.filter(pk=tu).first()
                ctxf.getTUinfo(tu, tc, ctx)
                return render(request, "tuc_addHW.html", ctx)
            elif who == 'teacher':
                ctxf.getTCinfo(tc, ctx)
            return render(request, "tc_addHW.html", ctx)
        elif doing == 'change':
            hw = request.POST['hw']
            hw = HW.objects.filter(pk=hw).first()
            hw.name = name
            hw.question = question
            hw.ift = ift
            if 'yes' in ift:
                times = request.POST['times']
                hw.times = times
            else:
                hw.times = 0
            hw.save()
            ctx['m1'] = '作业信息修改成功！'
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
        else:
            if 'yes' in ift:
                times = request.POST['times']
                HW.objects.create(name=name, question=question, times=times, TC=tc)
            else:
                HW.objects.create(name=name, question=question, times=0, TC=tc)
            ctx['m1'] = '成功发布作业！'
        who = request.POST['who']
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, tc, ctx)
            return render(request, "tuc_lookHW.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_lookHW.html", ctx)


def delete_hw(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        hw = request.POST['hw']
        hw = HW.objects.filter(pk=hw)
        if len(hw) == 0:
            ctx['m1'] = '作业不存在！'
        else:
            hw = hw.first()
            hw.delete()
            ctx['m1'] = '作业删除成功！'
        who = request.POST['who']
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, tc, ctx)
            return render(request, "tuc_lookHW.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_lookHW.html", ctx)


def free_solve(request):
    ctx = {}
    if request.POST:
        fa = request.POST['pk']
        fa = FreeApply.objects.filter(pk=fa).first()
        result = request.POST['result']

        if fa.read:
            ctx['m1'] = '该免修申请已处理！'
        elif result == 'yes':
            fa.read = True
            fa.accept = True
            fa.save()
            p = request.POST['point']
            sc = fa.SC
            sc.end = True
            sc.grade = p
            sc.free = True
            sc.save()
            ctx['m1'] = '已同意免修申请！'
        else:
            fa.read = True
            fa.accept = False
            fa.save()
            ctx['m1'] = '已拒绝免修申请！'

        ctxf.getTCinfo(fa.SC.TC, ctx)
    return render(request, "tc_free.html", ctx)


def read_do(request):
    ctx = {}
    if request.POST:
        hwd = request.POST['hwdid']
        hwd = HWD.objects.filter(pk=hwd).first()
        point = request.POST['point']
        back = request.POST['back']
        if ~hwd.read:
            ctx['m1'] = '成功评阅作业！'
        else:
            ctx['m1'] = '成功修改作业评阅！'

        hwd.back = back
        hwd.point = point
        hwd.read = True
        hwd.save()
        ctxf.getTCHWinfo(ctx, hwd.HW.TC, hwd.HW)
        who = request.POST['who']
        if who == 'tutor':
            tu = request.POST['TUno']
            tu = Student.objects.filter(pk=tu).first()
            ctxf.getTUinfo(tu, hwd.HW.TC, ctx)
            return render(request, "tuc_lookHW.html", ctx)
        elif who == 'teacher':
            ctxf.getTCinfo(hwd.HW.TC, ctx)
    return render(request, "tc_hw_detail.html", ctx)


def tc_judge_do(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()

        s = request.POST['sid']
        s = Student.objects.filter(pk=s).first()

        sc = SC.objects.filter(Sno=s, TC=tc).first()

        hwl = HW.objects.filter(TC=tc)
        hwd_l = []

        for i in hwl:
            one = {}
            one['title'] = i.name
            hwd = HWD.objects.filter(HW=i, Sno=s)
            if len(hwd) == 0:
                one['had'] = False
                one['read'] = False
                one['point'] = 0
            else:
                hwd = hwd.first()
                one['had'] = True
                one['read'] = hwd.read
                one['point'] = hwd.point
            hwd_l.append(one)

        ctxf.getTCinfo(tc, ctx)
        ctx['daily_p'] = sc.daily
        ctx['S'] = s
        ctx['hwd_l'] = hwd_l
    return render(request, "tc_judge_do.html", ctx)


def tc_judge_solve(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()

        s = request.POST['sid']
        s = Student.objects.filter(pk=s).first()
        grade = request.POST['grade']

        sc = SC.objects.filter(Sno=s, TC=tc).first()
        sc.grade = grade
        sc.end = True
        sc.save()

        ctx['m1'] = '打分完成！'

        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_judge.html", ctx)