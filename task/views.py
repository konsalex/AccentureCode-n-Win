from django.shortcuts import render,redirect
import json
import requests
from task.models import task,taskForm
from django.db import models
import sqlite3
import time

# Create your views here.





def task(request):

    if request.method=="POST":
        
        print (request.POST['taskname'])

        # conn = sqlite3.connect('/Users/ale/Desktop/task/Accenture/db.sqlite3')

        # c = conn.cursor()
        
            
        # stre="Insert into task_task VALUES ("+str(time.time())+","+request.POST['taskname']+","+request.POST['description']+","+request.POST['estimationdays']+","+request.POST['firstname']+","+request.POST['lastname']+","+request.POST['startingdate']+","+request.POST['endingdate']+","+request.POST['firstname2']+","+request.POST['lastname2']+","+request.POST['startingdate2']+","+request.POST['endingdate2']+")"")"

        # print (stre) 
        # c.execute(stre)

        # conn.commit()
        t=taskForm(request.POST)

        if t.is_valid():
            t.save()

        for key in request.POST:
            print(key)
        
        # t.save()





        # t=taskForm(request.POST)
        # print (t.cleaned_data)
        # if t.is_valid():
            
        #     print ("yes")
        
        # if t.is_valid():
        #     t.save()
        #     print("yes")
        # else:
        #     print("fucked")
        # temp.taskName=request.POST['taskname']
        # temp.description=request.POST['description']
        # temp.estimationDays=request.POST['estimationdays']
        # temp.p1First=request.POST['firstname']
        # temp.p1Last=request.POST['lastname']
        # temp.p1Start=request.POST['startingdate']
        # temp.p1End=request.POST['endingdate']

        # if 'firstname2' in request.POST and request.POST['firstname2']!="":
        #     temp.estimationDays=request.POST['estimationdays']
        #     temp.p2First=request.POST['firstname2']
        #     temp.p2Last=request.POST['lastname2']
        #     temp.p2Start=request.POST['startingdate2']
        #     temp.p2End=request.POST['endingdate2']

        # temp.save()

        
    
    return render(request,'index.html')