from django.urls import path
from . import views

app_name="task"
urlpatterns = [
    path("", views.index,name="index"),
    path("add/",views.addTask,name="add"),
    path("delete/",views.deleteTask,name="delete")
   
]