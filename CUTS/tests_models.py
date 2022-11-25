from django.test import TestCase
from .models import Supplier, Range, Roll, Cut

# Create your tests here.


class TestModels(TestCase):

    def test_supplier_returns_self(self):
        supplier = Supplier.objects.create(
            supplier='Test Supplier')
        self.assertEqual(str(supplier), 'Test Supplier')

    def test_range_returns_self(self):
        supplier = Supplier.objects.create(
            supplier='Test Supplier')
        ranges = Range.objects.create(
            supplier=supplier,
            ranges='Test Range')
        self.assertEqual(str(ranges), 'Test Range')

    def test_roll_returns_self(self):
        supplier = Supplier.objects.create(
            supplier='Test Supplier')
        ranges = Range.objects.create(
            supplier=supplier,
            ranges='Test Range')
        rolls = Roll.objects.create(
            ranges=ranges,
            rolls='Test Roll',
            roll_width='4m',
            roll_size='25',
            location='A1')
        self.assertEqual(str(rolls), 'Test Roll')

    def test_cut_returns_self(self):
        supplier = Supplier.objects.create(
            supplier='Test Supplier')
        ranges = Range.objects.create(
            supplier=supplier,
            ranges='Test Range')
        rolls = Roll.objects.create(
            ranges=ranges,
            rolls='Test Roll',
            roll_width='4m',
            roll_size='25',
            location='A1')
        cuts = Cut.objects.create(
            rolls=rolls,
            invoice='Test Invoice',
            cut_size='5')
        self.assertEqual(str(cuts), 'Test Invoice')
