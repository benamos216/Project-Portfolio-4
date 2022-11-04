from django import forms
from .models import Supplier, Range, Roll


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier']


class RangeForm(forms.ModelForm):
    class Meta:
        model = Range
        fields = ['supplier', 'ranges']


class RollForm(forms.ModelForm):
    class Meta:
        model = Roll
        fields = ['ranges', 'rolls', 'roll_width', 'roll_size', 'location']
