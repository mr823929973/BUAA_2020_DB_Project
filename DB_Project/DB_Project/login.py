# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse

from . import ctxf
import hashlib
import re


def toMD5(s):
    b = s.encode('gbk')
    return hashlib.md5(b).hexdigest()


def valid(s):
    s = str(s)
    v = re.search('^[0-9]+$', s)
    return v


# 接收POST请求数据
def top(request):
    ctx = {}
    ctx['m0'] = '请输入账号！'
    return render(request, "login.html", ctx)


def login(request):
    ctx = {}
    ctx['m0'] = '请输入账号！'
    if request.POST:
        user = request.POST['id']
        password = request.POST['password']
        pw = toMD5(str(user) + str(password))
        no = int(user)
        if 10000000 <= no < 100000000:
            student = Student.objects.filter(Sno=user)
            if len(student) == 0:
                ctx['m0'] = '账号不存在！'
                return render(request, "login.html", ctx)
            else:
                s1 = student.first()
                if pw != s1.pw:
                    ctx['m0'] = '密码错误！'
                    return render(request, "login.html", ctx)

                ctxf.getSinfo(s1, ctx)
                if Drop.objects.filter(Sno=s1, read=True, accept=True):
                    ctx['out'] = s1.Sno
                    return render(request, "drop_success.html", ctx)
                return render(request, "s_course.html", ctx)

        elif 10000 <= no < 100000:
            teacher = Teacher.objects.filter(Tno=user)
            if len(teacher) == 0:
                ctx['m0'] = '账号不存在！'
                return render(request, "login.html", ctx)
            else:
                t1 = teacher.first()
                if pw != t1.pw:
                    ctx['m0'] = '密码错误！'
                    return render(request, "login.html", ctx)

                ctxf.getTinfo(t1, ctx)
                return render(request, "t_top.html", ctx)
        elif no == 520:
            if pw != 'ff26716fe02f9ee1bf9af2b8e1aa05b9':
                ctx['m0'] = '权限密码错误！'
                return render(request, "login.html", ctx)
            else:
                ctxf.getManage(ctx)
                return render(request, "m_student.html", ctx)

    ctx['mo'] = '账号不存在！'
    return render(request, "login.html", ctx)
