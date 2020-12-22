# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse


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


# 接收POST请求数据
def top(request):
    ctx = {}
    ctx['m0'] = '请输入学工号！'
    return render(request, "login.html", ctx)


def login(request):
    ctx = {}
    ctx['m0'] = '请输入学工号！'
    if request.POST:
        user = request.POST['id']
        ty = request.POST['type']
        if ty == 'student':
            student = Student.objects.filter(Sno=user)
            if len(student) == 0:
                ctx['m0'] = '学号不存在！'
                return render(request, "login.html", ctx)
            else:
                getSinfo(student[0], ctx)
                return render(request, "top.html", ctx)
        elif ty == 'teacher':
            teacher = Teacher.objects.filter(Tno=user)
            if len(teacher) == 0:
                ctx['m0'] = '工号不存在！'
                return render(request, "login.html", ctx)
            else:
                getTinfo(teacher[0], ctx)
                return render(request, "top.html", ctx)
        elif ty == 'manage':
            if 
    return render(request, "login.html", ctx)
