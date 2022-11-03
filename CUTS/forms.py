from django import forms
from .models import Supplier, Range


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier']


class RangeForm(forms.ModelForm):
    class Meta:
        model = Range
        fields = ['ranges', 'supplier']
