from django.db import models


class Department(models.Model):
    Dno = models.IntegerField(primary_key=True)
    Dname = models.CharField(unique=True, max_length=20)


class Student(models.Model):
    Sno = models.IntegerField(primary_key=True)
    Sname = models.CharField(max_length=20)
    Dno = models.ForeignKey("Department", on_delete=models.CASCADE)


class Course(models.Model):
    Cno = models.IntegerField(primary_key=True, auto_created=True)
    Cname = models.CharField(unique=True, max_length=20)
    credit = models.IntegerField(default=2)
    v = models.IntegerField(default=3)


class TC(models.Model):
    Tno = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    Dno = models.ForeignKey("Department", on_delete=models.CASCADE)
    Cno = models.ForeignKey("Course", on_delete=models.CASCADE)


class Teacher(models.Model):
    Tno = models.IntegerField(primary_key=True)
    Tname = models.CharField(max_length=20)


class SC(models.Model):
    Sno = models.ForeignKey("Student", on_delete=models.CASCADE)
    TC = models.ForeignKey("TC", on_delete=models.CASCADE)
    free = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    grade = models.IntegerField(default=60)
    daily = models.IntegerField(default=60)
    Cno = models.ForeignKey("Course", on_delete=models.CASCADE)


class HW(models.Model):
    TC = models.ForeignKey("TC", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    question = models.CharField(max_length=50)
    times = models.IntegerField(default=0)


class HWD(models.Model):
    HW = models.ForeignKey("HW", on_delete=models.CASCADE)
    Sno = models.ForeignKey("Student", on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    read = models.BooleanField(default=False)
    point = models.FloatField(default=6)
    back = models.CharField(max_length=50)


class Tutor(models.Model):
    TC = models.ForeignKey("TC", on_delete=models.CASCADE)
    Sno = models.ForeignKey("Student", on_delete=models.CASCADE)


class FreeApply(models.Model):
    SC = models.ForeignKey("SC", on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    accept = models.BooleanField(default=False)
    reason = models.CharField(max_length=30)


class Plan(models.Model):
    Dno = models.ForeignKey("Department", on_delete=models.CASCADE)


class PlanD(models.Model):
    Pno = models.ForeignKey("Plan", on_delete=models.CASCADE)
    Cno = models.ForeignKey("Course", on_delete=models.CASCADE)


class Remark(models.Model):
    SC = models.ForeignKey("SC", on_delete=models.CASCADE)
    p0 = models.IntegerField(default=5)
    p1 = models.IntegerField(default=5)
    p2 = models.IntegerField(default=5)
    p3 = models.IntegerField(default=5)
    p4 = models.IntegerField(default=5)
    p5 = models.IntegerField(default=5)
    r = models.CharField(max_length=50)
    rec = models.BooleanField(default=True)

