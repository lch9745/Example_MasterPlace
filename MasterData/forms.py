from .models import Country_Data
from django import forms

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country_Data
        fields = ('name',)