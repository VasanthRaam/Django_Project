from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)

    def __str__(self):
        return self.fname+""+self.lname
class Myform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
