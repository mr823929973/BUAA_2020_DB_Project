# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
from . import ctxf


def tu_before(request):
    ctx = {}
    if request.POST:
        s = request.POST['TUno']
        s = Student.objects.filter(Sno=s).first()
        tul = Tutor.objects.filter(Sno=s)
        tuc_list = []
        for i in tul:
            one = {}
            one['Cn'] = i.TC.Cno.Cname
            one['Dn'] = i.TC.Dno.Dname
            one['Tn'] = i.TC.Tno.Tname
            one['credit'] = i.TC.Cno.credit
            one['s'] = SC.objects.filter(TC=i.TC).count()
            one['v'] = i.TC.Cno.v
            one['tid'] = i.TC.pk
            tuc_list.append(one)
        ctxf.getSinfo(s, ctx)
        ctx['tuc_list'] = tuc_list
    return render(request, "tu_before.html", ctx)



def add_tutor(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        sc = SC.objects.filter(TC=tc, Sno=s).first()
        conflict = Tutor.objects.filter(Sno=s, TC=tc)

        if len(conflict) != 0:
            ctx['m1'] = '该学生已是助教！'
        elif not sc.end:
            ctx['m1'] = '该学生还未完成该门课程！'
        else:
            Tutor.objects.create(Sno=s, TC=tc)
            ctx['m1'] = '成功设为助教！'
        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_top.html", ctx)


def delete_tutor(request):
    ctx = {}
    if request.POST:
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()

        Tutor.objects.filter(Sno=s, TC=tc).delete()
        ctx['m1'] = '解任助教成功！'
        ctxf.getTCinfo(tc, ctx)
    return render(request, "tc_top.html", ctx)