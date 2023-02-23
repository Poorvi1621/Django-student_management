
from django.contrib.auth.models import User
from datetime import datetime
from tkinter import CASCADE
from unicodedata import category
from django.db import models

class AddCourses(models.Model):
    course = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.course


class AddStudents(models.Model):
    sname = models.CharField(max_length=100)
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    saddress= models.CharField(max_length=255)
    scollege = models.CharField(max_length=255)
    sdegree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    scourse= models.ForeignKey(AddCourses, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.sname

class AddTeacher(models.Model):
    tname =models.CharField(max_length=100)
    tmail=models.EmailField(max_length=100)
    tmobile =models.CharField(max_length=10)
    taddress =models.TextField(max_length=100)
    alternate_mobile=models.CharField(max_length=10)
    experience =models.CharField(max_length=50)
    previous_salary =models.IntegerField(max_length=100)

    def __str__(self):
        return self.tname
