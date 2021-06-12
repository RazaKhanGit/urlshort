from django import forms
from .models import *

class urlForm(forms.ModelForm):
    class Meta:
        model = URLData
        fields = ['url']
class customURL(forms.ModelForm):
    class Meta:
        model = URLData
        fields = ['url', 'slug']