from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class task(models.Model):

    taskname=models.CharField(max_length=200,blank=False)

    description=models.TextField(blank=False)

    estimationdays=models.CharField(max_length=6,blank=False)

    p1First=models.CharField(max_length=100,blank=False,default=0)

    p1Last=models.CharField(max_length=100,blank=False,default=0)

    p1Start=models.CharField(max_length=100,blank=False,default=0)

    p1End=models.CharField(max_length=100,blank=False,default=0)

    p2First=models.CharField(max_length=100,blank=False,default=0,null=True)

    p2Last=models.CharField(max_length=100,blank=False,default=0,null=True)

    p2Start=models.CharField(max_length=100,blank=False,default=0,null=True)

    p2End=models.CharField(max_length=100,blank=False,default=0,null=True)

    def __str__(self):
        return self.taskname

class taskForm(ModelForm):

    p2First=forms.CharField(required=False)

    p2Last=forms.CharField(required=False)

    p2Start=forms.CharField(required=False)

    p2End=forms.CharField(required=False)
    
    class Meta:

        model=task

        fields = ['taskname','description','estimationdays','p1First','p1Last',
                        'p1Start','p1End','p2First','p2Last','p2Start','p2End']