from django.urls import re_path as url
from django.urls import path
from second_app import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('form/',views.form,name= "form"),
    # path('studentforms/',views.studentform,name ="studentforms"),
    # path('teachers/',views.Teacherinfo,name = "teachers")
]

