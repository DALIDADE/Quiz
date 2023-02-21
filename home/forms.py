from django import forms
from .views import *

class TestMaglumatlaryForm(forms.ModelForm):
    class Meta:
        model = TestMaglumatlary
        fields = '__all__'

class TestGosmakForm(forms.ModelForm):
    class Meta:
        model = TestGosmak
        fields = '__all__'