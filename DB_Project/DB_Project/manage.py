# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse


def getManage(ctx):
    department = Department.objects.all()
    d_list = []
    for i in department:
        one = {}
        one['Dno'] = i.Dno
        one['Dname'] = i.Dname
        d_list.append(one)
    ctx['d_list'] = d_list
    ctx['t'] = 'manager'


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

def getSinfo(s, ctx):
    sc = SC.objects.filter(Sno=s.Sno)
    had = []
    had_Cno = []
    can = []
    for i in sc:
        one = {}
        one['Cn'] = i.TC.Cno.Cname
        one['Cno'] = i.TC.Cno.Cno
        one['Tn'] = i.TC.Tno.Tname
        one['grade'] = i.grade
        one['end'] = i.end
        had_Cno.append(i.TC.Cno.Cno)
        had.append(one)
    tc = TC.objects.filter(Dno=s.Dno)
    for i in tc:
        if i.Cno.Cno not in had_Cno:
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
            can.append(one)
    ctx['c_list'] = had
    ctx['c_select'] = can
    ctx['t'] = 'student'
    ctx['user'] = s


def m_refresh(request):
    ctx = {}
    getManage(ctx)
    return render(request, "manage.html", ctx)


def m_delete_all(request):
    ctx = {}
    if request.POST:
        SC.objects.all().delete()
        TC.objects.all().delete()
        Student.objects.all().delete()
        Department.objects.all().delete()
        Course.objects.all().delete()
        Teacher.objects.all().delete()

        Teacher.objects.create(Tno=99999, Tname='Tony')
        Course.objects.create(Cno=119, Cname='海阳秧歌初级', credit=100, v=100)
        d = Department.objects.create(Dno=114514, Dname='阿兹卡班')
        Student.objects.create(Sno=1919810, Sname='魔仙小月', Dno=d)
        ctx['m1'] = '重 置 成 功！'
    getManage(ctx)
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
    getManage(ctx)
    return render(request, "manage.html", ctx)


def m_add_teacher(request):
    ctx = {}
    if request.POST:
        Tno = request.POST['Tno']
        Tname = request.POST['Tname']
        Teacher.objects.create(Tno=Tno, Tname=Tname)
        # SC.objects.create(Sno=s, Cno=t.Cno, TC=t)
        ctx['m1'] = '录 入 老 师 成 功！'
    getManage(ctx)
    return render(request, "manage.html", ctx)


def m_add_department(request):
    ctx = {}
    if request.POST:
        Dno = request.POST['Dno']
        Dname = request.POST['Dname']
        Department.objects.create(Dno=Dno, Dname=Dname)
        # SC.objects.create(Sno=s, Cno=t.Cno, TC=t)
        ctx['m1'] = '又 要 修 新 楼 了！'
    getManage(ctx)
    return render(request, "manage.html", ctx)


def m_delete_all_t(request):
    ctx = {}
    SC.objects.all().delete()
    TC.objects.all().delete()
    Student.objects.all().delete()
    Department.objects.all().delete()
    Course.objects.all().delete()
    Teacher.objects.all().delete()
    ctx['m1'] = '我们的王回来了！！！'
    getManage(ctx)
    return render(request, "manage.html", ctx)
