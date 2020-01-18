from django import forms
from responseapp.models import Response

class MyForm(forms.ModelForm):
 name = forms.CharField(label='Name', max_length=100)
 color = forms.CharField(label='Favorite Color', max_length=100)
 pet = forms.CharField(label='Cats or Dogs', max_length=100)

 class Meta:
     model = Response
     fields = ('name', 'color', 'pet')

