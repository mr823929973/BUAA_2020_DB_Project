from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse
import random
from django.db.models import Avg

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
        r = Remark.objects.filter(SC=i)
        one['hadR'] = len(r) != 0
        one['Cn'] = i.TC.Cno.Cname
        one['Cno'] = i.TC.Cno.Cno
        one['Tn'] = i.TC.Tno.Tname
        one['grade'] = i.grade
        one['end'] = i.end
        one['free'] = i.free
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

    hwl = HW.objects.filter(TC=tc)
    ctx['hw_times'] = hwl.count()

    sl = SC.objects.filter(TC=tc)
    s_list = []
    for i in sl:
        one = {}
        one['end'] = i.end
        one['Sn'] = i.Sno.Sname
        one['free'] = i.free
        one['grade'] = i.grade
        one['Sno'] = i.Sno.Sno
        one['dailyend'] = i.dailyend
        one['daily'] = i.daily
        one['hwtime'] = HWD.objects.filter(Sno=i.Sno, HW__TC=tc).count()
        readHW = HWD.objects.filter(Sno=i.Sno, HW__TC=tc, read=True)
        avg = 0
        for j in readHW:
            avg += j.point
        if len(readHW) == 0:
            one['avghw'] = 0
        else:
            one['avghw'] = avg / len(readHW)
        s_list.append(one)
    ctx['s_list'] = s_list

    hw_list = []
    for i in hwl:
        one = {}
        one['times'] = i.times
        one['name'] = i.name
        one['hwid'] = i.pk
        one['done'] = HWD.objects.filter(HW=i).count()
        hw_list.append(one)
    ctx['hw_list'] = hw_list

    fl = FreeApply.objects.filter(SC__TC=tc)
    free_list = []
    for i in fl:
        one = {}
        one['free'] = i
        one['pk'] = i.pk
        one['Sn'] = i.SC.Sno.Sname
        one['Dn'] = i.SC.TC.Dno.Dname
        one['read'] = i.read
        one['accept'] = i.accept
        free_list.append(one)
    ctx['free_list'] = free_list

    tutor = Tutor.objects.filter(TC=tc)
    tutor_list = []
    for i in tutor:
        tutor_list.append(i.Sno.Sno)
    ctx['tutor_list'] = tutor_list


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
    r = Remark.objects.filter(SC=sc)
    ctx['hadR'] = len(r) != 0

    hwl = HW.objects.filter(TC=sc.TC)
    hw_list = []
    for i in hwl:
        one = {}
        hwdl = HWD.objects.filter(Sno=sc.Sno, HW=i)
        one['name'] = i.name
        one['times'] = i.times
        one['hwid'] = i.pk
        if len(hwdl) != 0:
            one['had'] = True
            hwdl = hwdl.first()
            one['times_had'] = hwdl.had
            one['hwdid'] = hwdl.pk
            one['read'] = hwdl.read
            one['point'] = hwdl.point
        else:
            one['had'] = False
            one['times_had'] = 0
        hw_list.append(one)

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

    drop = Drop.objects.all()
    drop_list = []
    for i in drop:
        one = {}
        one['did'] = i.pk
        one['Dn'] = i.Sno.Dno.Dname
        one['Sn'] = i.Sno.Sname
        one['read'] = i.read
        one['accept'] = i.accept
        drop_list.append(one)
    ctx['drop_list'] = drop_list

    change = Change.objects.all()
    change_list = []
    for i in change:
        one = {}
        one['cid'] = i.pk
        one['Dn'] = i.Sno.Dno.Dname
        one['Dn2'] = i.Dno.Dname
        one['Sn'] = i.Sno.Sname
        one['read'] = i.read
        one['accept'] = i.accept
        change_list.append(one)
    ctx['change_list'] = change_list

    ctx['t'] = 'manager'

    te = Teacher.objects.all()
    t_table = []
    for i in te:
        one = {}
        one['open'] = TC.objects.filter(Tno=i).count()
        one['Tname'] = i.Tname
        re = Remark.objects.filter(SC__TC__Tno=i)
        a = 0
        for j in re:
            a += j.p3
        if len(re) == 0:
            a = 0
        else:
            a = a/len(re)
        one['re'] = a
        t_table.append(one)
    ctx['t_table'] = t_table

    st = Student.objects.all()
    s_table = []
    for i in st:
        one = {}
        one['Sname'] = i.Sname
        one['Dname'] = i.Dno.Dname
        selected = SC.objects.filter(Sno=i)
        se = len(selected)
        end = 0
        p = 0
        cre = 0
        for j in selected:
            if j.end:
                end += 1
                cre += j.TC.Cno.credit
                p += j.grade * j.TC.Cno.credit
        if cre == 0:
            one['p'] = 0
        else:
            one['p'] = p / cre
        one['se'] = se
        one['end'] = end
        one['cre'] = cre
        s_table.append(one)
    sorted(s_table, key=lambda x: (x['cre']))
    ctx['s_table'] = s_table

    co = TC.objects.all()
    c_table = []

    for i in co:
        one = {}
        one['Cname'] = i.Cno.Cname
        one['Tname'] = i.Tno.Tname
        one['Dname'] = i.Dno.Dname
        sec = SC.objects.filter(TC = i)
        se = len(sec)
        end = 0
        p0 = 0
        r1 = 0
        r2 = 0
        r3 = 0
        for j in sec:
            if j.end:
                end += 1
                p0 += j.grade
                if j.grade < 60:
                    r1 += 1
                elif 60 <= j.grade < 80:
                    r2 += 1
                else:
                    r3 += 1
        if end == 0:
            one['p0'] = 0
            one['r1'] = 0
            one['r2'] = 0
            one['r3'] = 0
        else:
            one['p0'] = p0 / end
            one['r1'] = r1 / end * 100
            one['r2'] = r2 / end * 100
            one['r3'] = r3 / end * 100
        one['se'] = se
        one['end'] = end

        c_table.append(one)

    ctx['c_table'] = c_table

def getTCHWinfo(ctx, tc, hw):
    ctx['hw'] = hw
    hwds = HWD.objects.filter(HW=hw)
    ctx['done'] = hwds.count()

    scs = SC.objects.filter(TC=tc)
    s_hw_list = []
    for i in scs:
        one = {}
        one['Sn'] = i.Sno.Sname
        hwd_now = hwds.filter(Sno=i.Sno)
        one['Sno'] = i.Sno.Sno
        if len(hwd_now) == 0:
            one['had_time'] = 0
        else:
            hwd_now = hwd_now.first()
            one['had_time'] = hwd_now.had
            one['read'] = hwd_now.read
            one['point'] = hwd_now.point
        s_hw_list.append(one)
    ctx['s_hw_list'] = s_hw_list


def getTUinfo(s, tc, ctx):
    ctx['C'] = tc.Cno
    ctx['D'] = tc.Dno
    ctx['T'] = tc.Tno
    ctx['se'] = SC.objects.filter(TC=tc).count()
    ctx['tid'] = tc.pk
    hwl = HW.objects.filter(TC=tc)
    ctx['hw_times'] = hwl.count()
    sl = SC.objects.filter(TC=tc)
    s_list = []
    for i in sl:
        one = {}
        one['end'] = i.end
        one['Sn'] = i.Sno.Sname
        one['free'] = i.free
        one['grade'] = i.grade
        one['Sno'] = i.Sno.Sno
        one['dailyend'] = i.dailyend
        one['daily'] = i.daily
        one['hwtime'] = HWD.objects.filter(Sno=i.Sno, HW__TC=tc).count()
        readHW = HWD.objects.filter(Sno=i.Sno, HW__TC=tc, read=True)
        avg = 0
        for j in readHW:
            avg += j.point
        if len(readHW) == 0:
            one['avghw'] = 0
        else:
            one['avghw'] = avg / len(readHW)
        s_list.append(one)
    ctx['s_list'] = s_list

    hw_list = []
    for i in hwl:
        one = {}
        one['times'] = i.times
        one['name'] = i.name
        one['hwid'] = i.pk
        one['done'] = HWD.objects.filter(HW=i).count()
        hw_list.append(one)
    ctx['hw_list'] = hw_list
    ctx['user'] = s
