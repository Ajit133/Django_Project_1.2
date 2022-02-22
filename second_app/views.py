from multiprocessing import context
from operator import index
import re
from turtle import update
from unicodedata import name
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import Musician,Album
from second_app import forms

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'musician':musician_list,"text_1":"i am programmar"}
    return render(request,'index.html',context=diction)

def form(request):
    new_form = forms.MusicianForm()
    
    
    if request.method == "POST":
        new_form = forms.MusicianForm(request.POST)
        # diction.update({"test_form": new_form})
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction = {"test_form":new_form}
    return render(request,"form.html",context=diction)






# def Teacherinfo(request):
#     new_form = forms.teacharForm()
#     diction = {"info":new_form}

#     if request.method == "POST":
#         new_form = forms.teacharForm(request.POST)
#         if new_form.is_valid():
#             teacher_name = new_form.cleaned_data['teacher_name']
#             teacher_email = new_form.cleaned_data['teacher_email']
#             teacher_Dob = new_form.cleaned_data['teacher_Dob']

#             diction.update({'teacher_name':teacher_name})
#             diction.update({'teacher_email':teacher_email})
#             diction.update({'teacher_Dob':teacher_Dob})
#             diction.update({"Submitted":"This Form is submitted"})



#     return render(request,"teacher_forms.html",context=diction)

