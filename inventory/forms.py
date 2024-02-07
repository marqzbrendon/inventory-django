# inventory/forms.py
from django import forms

class ItemForm(forms.Form):
    item = forms.CharField(max_length=100)
    quantity = forms.IntegerField(min_value=0)

class AccessForm(forms.Form):
    user = forms.CharField(max_length=25)
    code = forms.CharField(max_length=20)