from django.shortcuts import get_object_or_404, render
from django import forms
# Create your views here.

class optionform(forms.Form):
    theme = forms.CharField(max_length=200)
    option1_text = forms.CharField(max_length=200)
    option2_text = forms.CharField(max_length=200)
