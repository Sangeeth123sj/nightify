from django import forms
from main.models import Picture

class UploadForm(forms.Form):
    upload = forms.ImageField()