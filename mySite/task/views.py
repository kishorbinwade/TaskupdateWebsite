from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class newTaskForm(forms.Form):
    tasks=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Priority",min_value=1,max_value=5)
    #delete_tasks=forms.CharField(label="Delete task",blank=True)
    #CHOICES = [('yes', 'Yes'), ('no', 'No')]
    #delete_tasks=forms.CharField(label="Do you want delete task",widget=forms.RadioSelect(choices=CHOICES))
    

    
'''
    if delete_tasks=='yes':
        delete_task_input=forms.CharField(label="Enter deletion task")
    else:
        None    
'''

class deleteForm(forms.Form):
    delete_tasks=forms.CharField(label="Delete task",required=False)

    

def index(request):
    if "task" not in request.session:  
        request.session["task"]=[]              #request.session["task"] used here to not repeat same content to another web page.
    return render(request,"task/index.html",{
        "task":request.session["task"]
    })

def addTask(request):
    if request.method=="POST":
        form=newTaskForm(request.POST)
        if form.is_valid():
            task_list=request.session["task"]
            Updated_task=form.cleaned_data["tasks"]
            task_list+=[Updated_task]
            #request.session["task"]+=[Updated_task]
           
            request.session.modified = True    

            

        

                            


            return HttpResponseRedirect(reverse("task:index")) #to go reverse and check task index page 
        else:
            return render(request,"task/add.html",{
                "form":form
            })    
    return render(request,"task/add.html", {
        "form":newTaskForm()
    }
    ) 
      

def deleteTask(request):
    """
    if request.method=="POST":
        form=deleteForm(request.POST)
        if form.delete_tasks.is_valid:
            delete_task1=form.cleaned_data["delete_tasks"]
    
            if delete_task1 not in  task_list :
                pass
            else:    
                task_list.remove(delete_task1)
          return HttpResponseRedirect(reverse("task:index")) 
"""
    if request.method=="POST":
        form=deleteForm(request.POST)
        if form.is_valid():
            task_list=request.session["task"]
            delete_task1=form.cleaned_data["delete_tasks"]
            if delete_task1 not in  task_list :
                pass
            else:    
                task_list.remove(delete_task1)
           
            request.session.modified = True    

            return HttpResponseRedirect(reverse("task:index")) #to go reverse and check task index page 
        else:
            return render(request,"task/delete.html",{
                "form":form
            })    
    return render(request,"task/delete.html", {
        "form":deleteForm()
    }
    )      

