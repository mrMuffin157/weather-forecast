from django import forms
from home.models import weather

class LocationForm(forms.Form):
    city = forms.CharField()