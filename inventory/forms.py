# inventory/forms.py
from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    quantity = forms.IntegerField(min_value=0)

class AccessForm(forms.Form):
    user = forms.CharField(max_length=100)
    code = forms.IntegerField(max_value=999999)