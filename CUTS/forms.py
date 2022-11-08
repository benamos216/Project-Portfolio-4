from django import forms
from .models import Supplier, Range, Roll, Cut


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


class CutForm(forms.ModelForm):
    class Meta:
        model = Cut
        fields = ['rolls', 'invoice', 'cut_size']
