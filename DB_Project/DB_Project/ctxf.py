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
        one['scid'] = i.pk
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


def getTCinfo(tc, ctx):
    ctx['C'] = tc.Cno
    ctx['D'] = tc.Dno
    ctx['T'] = tc.Tno
    ctx['se'] = SC.objects.filter(TC=tc).count()
    ctx['user'] = tc.Tno
    ctx['tid'] = tc.pk

    sl = SC.objects.filter(TC=tc)
    s_list = []
    for i in sl:
        one = {}
        one['end'] = i.end
        one['Sn'] = i.Sno.Sname
        s_list.append(one)
    ctx['s_list'] = s_list

    hwl = HW.objects.filter(TC=tc)
    hw_list = hwl
    # for i in hwl:
    #     one = {}
    ctx['hw_list'] = hw_list


def getSCinfo(sc, ctx):
    ctx['T'] = sc.TC.Tno
    ctx['TC'] = sc.TC
    ctx['S'] = sc.Sno
    ctx['D'] = sc.TC.Dno
    ctx['user'] = sc.Sno
    ctx['sc'] = sc
    ctx['scid'] = sc.pk
    ctx['C'] = sc.TC.Cno
    ctx['se'] = SC.objects.filter(TC=sc.TC).count()

    hwl = HW.objects.filter(TC=sc.TC)
    hw_list = hwl
    # for i in hwl:
    #     one = {}
    ctx['hw_list'] = hw_list



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