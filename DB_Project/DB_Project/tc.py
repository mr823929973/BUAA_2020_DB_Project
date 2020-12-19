# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
import random


def getCno():
    i = random.randint(0, 100000)
    while len(Course.objects.filter(Cno=i)) != 0:
        i = random.randint(0, 100000)
    return i


def getTinfo(t, ctx):
    tc = TC.objects.filter(Tno=t.Tno)
    tc_list = []
    for i in tc:
        one = {}
        one['Cno'] = i.Cno.Cno
        one['Tn'] = i.Tno.Tname
        one['Tno'] = i.Tno.Tno
        one['Cn'] = i.Cno.Cname
        one['Dno'] = i.Dno.Dno
        one['Dn'] = i.Dno.Dname
        one['credit'] = i.Cno.credit
        one['tid'] = i.pk
        one['v'] = i.Cno.v
        one['s'] = SC.objects.filter(TC=i.pk).count()
        tc_list.append(one)

    ctx['tc_list'] = tc_list
    ctx['d_list'] = Department.objects.all()
    ctx['cs_list'] = Course.objects.all()
    ctx['t'] = 'teacher'
    ctx['user'] = t


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
        getSinfo(s, ctx)
    return render(request, "top.html", ctx)


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
        getSinfo(s, ctx)
    return render(request, "top.html", ctx)


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
        getTinfo(t, ctx)
    return render(request, "top.html", ctx)


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
        getTinfo(t, ctx)
    return render(request, "top.html", ctx)
