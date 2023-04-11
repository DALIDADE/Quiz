from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .views import *

# class TalypForm(UserCreationForm):
#     topary = forms.IntegerField(required=True)

#     class Meta:
#         models =User
#         fields = ("username", "topary", "password1", "password2")

#     def save(self,commit=True):
#         user = super(TalypForm,self).save(commit=False)
#         user.topary = self.cleaned_data['topary']
#         if commit :
#             user.save()


class TestMaglumatlaryForm(forms.ModelForm):
    class Meta:
        model = TestMaglumatlary
        fields = ('Sapagyn_ady',
                 'Testin_ady',
                 'Topar',
                 'Sorag_sany',
                 'Wagyt_limidi')




class TestGosmakForm(forms.ModelForm):
    class Meta:
        model = TestGosmak
        fields = ('Soragy',
                 'a',
                 'b',
                 'c',
                 'dogry')