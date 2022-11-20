from django.test import TestCase
from .models import Supplier, Range, Roll, Cut

# Create your tests here.


class TestModels(TestCase):

    def test_supplier_returns_self(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        self.assertEqual(str(supplier), 'Test Supplier')

    def test_range_returns_self(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(ranges='Test Range')
        ranges = Range.objects.get(id=1)
        self.assertEqual(str(ranges), 'Test Range')

    # def test_roll_returns_self(self):
    #     rolls = Roll.objects.create(rolls='Test Roll')
    #     self.assertEqual(str(rolls), 'Test Roll')

    # def test_cut_returns_self(self):
    #     cuts = Cut.objects.create(invoice='Test Invoice')
    #     self.assertEqual(str(cuts), 'Test invoice')
