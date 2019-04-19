from django.db import models
from django.utils import timezone
import datetime

class Faculty(models.Model):
    f_id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    dept = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.CharField(primary_key=True,max_length=200)
    title = models.CharField(max_length=200)
    dept = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    dept = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Takes(models.Model):
    roll_no = models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.IntegerField()
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.roll_no.name + '->'+self.course_id.title

class Teaches(models.Model):
    f_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    semester = models.IntegerField()

    def __str__(self):
        return self.f_id.name + '->'+self.course_id.title

class Feedback(models.Model):
    f_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q13 = models.IntegerField()
    q14 = models.IntegerField()
    q15 = models.IntegerField()
    comment = models.TextField()
    average = models.FloatField()

    def __str__(self):
        return self.f_id.name + '->'+self.course_id.title


class Attendance(models.Model):
    roll_no = models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    P_A = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
