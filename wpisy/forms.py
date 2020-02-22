from django import forms 
from . import models 

class NowyWpis(forms.ModelForm):
    class Meta:
        model = models.Wpis
        fields = ['title', 'body', 'slug', 'thumb']