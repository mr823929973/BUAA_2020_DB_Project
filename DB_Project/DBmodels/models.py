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
    Cno = models.ForeignKey("Course", on_delete=models.CASCADE)


# class HW(models.Model):
#     TC = models.ForeignKey("TC", on_delete=models.CASCADE)