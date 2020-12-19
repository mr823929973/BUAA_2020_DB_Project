# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse


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
        getSinfo(s, ctx)
    return render(request, "top.html", ctx)
