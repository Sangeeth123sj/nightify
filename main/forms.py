from django import forms
from django.contrib.auth.forms import UserCreationForm


class UploadForm(forms.Form):
    upload = forms.ImageField()
    
