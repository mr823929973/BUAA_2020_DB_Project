# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.views.decorators import csrf
from DBmodels.models import *
from django.http import HttpResponse

from . import ctxf


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
                ctxf.getSinfo(student[0], ctx)
                return render(request, "s_top.html", ctx)
        elif ty == 'teacher':
            teacher = Teacher.objects.filter(Tno=user)
            if len(teacher) == 0:
                ctx['m0'] = '工号不存在！'
                return render(request, "login.html", ctx)
            else:
                ctxf.getTinfo(teacher[0], ctx)
                return render(request, "t_top.html", ctx)
        elif ty == 'manager':
            if user != "kumomo":
                ctx['m0'] = '权限密码错误！'
                return render(request, "login.html", ctx)
            else:
                ctxf.getManage(ctx)
                return render(request, "manage.html", ctx)
    return render(request, "login.html", ctx)
