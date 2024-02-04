# inventory/forms.py
from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    quantity = forms.IntegerField(min_value=0)
