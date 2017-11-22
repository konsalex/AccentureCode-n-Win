from django import forms
from task.models import task


class taskForm(ModelForm):
    
    taskName=forms.CharField(max_length=100,required=True)
    description=forms.CharField(required=True)
    estimationDays=forms.CharField(max_length=6,required=True)
    p1First=forms.CharField(max_length=100,required=True)
    p1Last=forms.CharField(max_length=100,required=True)
    p1Start=forms.CharField(max_length=60,required=True)
    p1End=forms.CharField(max_length=60,required=True)
    p2First=forms.CharField(max_length=100,required=False)
    p2Last=forms.CharField(max_length=100,required=False)
    p2Start=forms.CharField(max_length=60,required=False)
    p2End=forms.CharField(max_length=60,required=False)

    class Meta:
        model = task
        fields = ('taskName','description','estimationDays','p1First','p1Last','p1Start','p1End','p2First','p2Last','p2Start','p2End')
