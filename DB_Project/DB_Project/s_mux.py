# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse

from . import ctxf


def s_select(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        ctxf.getSinfo(s, ctx)
    return render(request, "s_select.html", ctx)


def s_top(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        ctxf.getSinfo(s, ctx)
    return render(request, "s_top.html", ctx)


def s_course(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        ctxf.getSinfo(s, ctx)
    return render(request, "s_course.html", ctx)


def sc_detail(request):
    ctx = {}
    if request.POST:
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        ctxf.getSCinfo(sc, ctx)
    return render(request, "sc_top.html", ctx)


def sc_lookHW(request):
    ctx = {}
    if request.POST:
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        ctxf.getSCinfo(sc, ctx)
    return render(request, "sc_lookHW.html", ctx)


def sc_doHW(request):
    ctx = {}
    if request.POST:
        hw = request.POST['hwid']
        hw = HW.objects.filter(pk=hw)
        s = request.POST['Sno']
        s = Student.objects.filter(pk=s).first()
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        ctxf.getSCinfo(sc, ctx)

        if len(hw) == 0:
            ctx['m1'] = '作业不存在！'
            return render(request, "sc_lookHW.html", ctx)
        hw = hw.first()

        ctx['hw'] = hw
        hwd = HWD.objects.filter(HW=hw, Sno=s)
        if len(hwd) == 0:
            ctx['hwd_read'] = False
            ctx['had_time'] = 0
            ctx['hw_content'] = ''
        else:
            ctx['hwd_read'] = hwd.first().read
            ctx['hwd_point'] = hwd.first().point
            ctx['had_time'] = hwd.first().had
            ctx['hwd'] = hwd.first()
            ctx['hw_content'] = hwd.first().content
    return render(request, "sc_HW_detail.html", ctx)


def s_drop(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        one = {}
        one['Sname'] = s.Sname
        one['Sno'] = s.Sno
        one['Dname'] = s.Dno.Dname

        ctx['er'] = one
        ctxf.getSinfo(s, ctx)
    return render(request, "s_drop.html", ctx)


def s_remark_do(request):
    ctx = {}
    if request.POST:
        sc = request.POST['sc']
        sc = SC.objects.filter(pk=sc).first()
        ctxf.getSCinfo(sc, ctx)
    return render(request, "s_remark_do.html", ctx)


def s_Dchange(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        one = {}
        one['Sname'] = s.Sname
        one['Sno'] = s.Sno
        one['Dname'] = s.Dno.Dname
        dl = Department.objects.exclude(Dno=s.Dno.Dno)
        ctx['d_list'] = dl
        ctx['er'] = one
        ctxf.getSinfo(s, ctx)
    return render(request, "s_Dchange.html", ctx)


def s_remark_top(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        ctxf.getSinfo(s, ctx)
    return render(request, "s_remark_top.html", ctx)


def s_change_top(request):
    ctx = {}
    if request.POST:
        s = request.POST['Sno']
        s = Student.objects.filter(Sno=s).first()
        ctxf.getSinfo(s, ctx)
    return render(request, "s_change_top.html", ctx)


def sc_c_detail(request):
    ctx = {}
    if request.POST:
        s = request.POST['user']
        tc = request.POST['tc']
        tc = TC.objects.filter(pk=tc).first()
        s = Student.objects.filter(Sno=s).first()

        rs = Remark.objects.filter(SC__TC=tc)
        rsT = Remark.objects.filter(SC__TC__Tno=tc.Tno)
        ctx['rs'] = rs
        rsn = len(rs)
        rstn = len(rsT)
        rr = {}
        p0 = 0
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        rec = 0
        for i in rs:
            p0 += i.p0
            p1 += i.p1
            p2 += i.p2
            if i.rec:
                rec += 1
        for i in rsT:
            p3 += i.p3
            p4 += i.p4
            p5 += i.p5
        if rsn == 0:
            rr['p0'] = 0
            rr['p1'] = 0
            rr['p2'] = 0
            rr['rec'] = 0
        else:
            rr['p0'] = p0 / rsn
            rr['p1'] = p1 / rsn
            rr['p2'] = p2 / rsn
            rr['rec'] = rec / rsn * 100
        if rstn == 0:
            rr['p3'] = 0
            rr['p4'] = 0
            rr['p5'] = 0
        else:
            rr['p3'] = p3 / rstn
            rr['p4'] = p4 / rstn
            rr['p5'] = p5 / rstn
        ctx['rr'] = rr
        ctx['Cname'] = tc.Cno.Cname
        ctx['Tname'] = tc.Tno.Tname
        ctx['Dname'] = tc.Dno.Dname
        ctxf.getSinfo(s, ctx)
    return render(request, "sc_c_detail.html", ctx)