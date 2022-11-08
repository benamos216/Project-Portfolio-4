from django.test import TestCase
from .forms import SupplierForm, RangeForm, RollForm, CutForm

# Create your tests here.


class TestSupplierForm(TestCase):

    def test_supplier_is_required(self):
        form = SupplierForm{{'supplier':''}}
        self.assertFalse(form.is_valid())
        self.assertIn('supplier', form.errors.keys())
        self.assertEqual(form.errors['supplier'][0], 'This field is required.')
