from django import forms
from .models import *
class NetijeForm(forms.ModelForm):
    class Meta:
        model = Netijeler
        fields = ('Topar',
                  'user',
                  'Dersin_ady',
                  'Dogry_sany',
                  'Yalnys_sany',
                  )

