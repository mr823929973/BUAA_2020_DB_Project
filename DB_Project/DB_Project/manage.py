# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse

from . import ctxf


def delete_all():
    FreeApply.objects.all().delete()
    Tutor.objects.all().delete()
    HWD.objects.all().delete()
    HW.objects.all().delete()
    SC.objects.all().delete()
    TC.objects.all().delete()
    Student.objects.all().delete()
    Department.objects.all().delete()
    Course.objects.all().delete()
    Teacher.objects.all().delete()


def initial():
    Teacher.objects.create(Tno=99999, Tname='Tony')
    Course.objects.create(Cno=119, Cname='海阳秧歌初级', credit=100, v=100)
    d = Department.objects.create(Dno=114514, Dname='阿兹卡班')
    Student.objects.create(Sno=1919810, Sname='魔仙小月', Dno=d)


def m_refresh(request):
    ctx = {}
    ctxf.getManage(ctx)
    return render(request, "manage.html", ctx)


def m_delete_all(request):
    ctx = {}
    if request.POST:
        delete_all()
        initial()
        ctx['m1'] = '重 置 成 功！'
    ctxf.getManage(ctx)
    return render(request, "manage.html", ctx)


def m_add_student(request):
    ctx = {}
    if request.POST:
        Sno = request.POST['Sno']
        Sname = request.POST['Sname']
        Dno = request.POST['Dno']
        Dno = Department.objects.filter(Dno=Dno).first()
        Student.objects.create(Sno=Sno, Sname=Sname, Dno=Dno)
        # SC.objects.create(Sno=s, Cno=t.Cno, TC=t)
        ctx['m1'] = '开 始 坐 牢！'
    ctxf.getManage(ctx)
    return render(request, "manage.html", ctx)


def m_add_teacher(request):
    ctx = {}
    if request.POST:
        Tno = request.POST['Tno']
        Tname = request.POST['Tname']
        Teacher.objects.create(Tno=Tno, Tname=Tname)
        # SC.objects.create(Sno=s, Cno=t.Cno, TC=t)
        ctx['m1'] = '录 入 老 师 成 功！'
    ctxf.getManage(ctx)
    return render(request, "manage.html", ctx)


def m_add_department(request):
    ctx = {}
    if request.POST:
        Dno = request.POST['Dno']
        Dname = request.POST['Dname']
        Department.objects.create(Dno=Dno, Dname=Dname)
        # SC.objects.create(Sno=s, Cno=t.Cno, TC=t)
        ctx['m1'] = '又 要 修 新 楼 了！'
    ctxf.getManage(ctx)
    return render(request, "manage.html", ctx)


def m_delete_all_t(request):
    ctx = {}
    delete_all()
    ctx['m1'] = '我们的王回来了！！！'
    ctxf.getManage(ctx)
    return render(request, "manage.html", ctx)
