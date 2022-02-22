from asyncio import events
from xmlrpc.client import boolean
from django import forms
from django.core import validators
from second_app import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"


    
# class Ex(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
    # number_field = forms.IntegerField(validators=[validators.MaxValueValidator(20),validators.MinValueValidator(11)])
    # custome forms 
    
# def even(value):
#         if value % 2 != 0:
#             raise forms.ValidationError('%(value)s is not an even number')

# class user_form(forms.Form):
#         number_fields = forms.IntegerField(validators=[even])
# class user_form(forms.Form):
#     user_email = forms.EmailField()
#     user_vmail = forms.EmailField()

#     def clean(self):
#         all_cleaned_data = super().clean()
#         user_email = all_cleaned_data['user_email']
#         user_vmail = all_cleaned_data['user_vmail']

#         if user_email != user_vmail:
#             raise forms.ValidationError("Fields Don't Match")


    

