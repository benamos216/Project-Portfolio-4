from django.test import TestCase
from http import HTTPStatus
from django.shortcuts import reverse
from .forms import SupplierForm, RangeForm, RollForm, CutForm
from .models import Supplier, Range, Roll, Cut

# Create your tests here.


class TestViews(TestCase):

    def test_get_supplier_renders(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'supplier.html')

    def test_add_supplier(self):
        response = self.client.post('/add_supplier', {'supplier': 'Test Supplier'})
        self.assertRedirects(response, '/')

    def test_SupplierForm_context(self):
        response = self.client.get(reverse('add_supplier'))
        self.assertIsInstance(response.context['form'], SupplierForm)

    def test_edit_supplier(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        response = self.client.get(f'/edit_supplier/{supplier.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_supplier.html')

    def test_delete_supplier(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        response = self.client.get(f'/delete_supplier/{supplier.id}')
        self.assertRedirects(response, '/')
        existing_items = Supplier.objects.filter(id=supplier.id)
        self.assertEqual(len(existing_items), 0)

    def test_get_ranges(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        response = self.client.get(f'/get_ranges/{supplier.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ranges.html')

    def test_edit_ranges(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        response = self.client.get(f'/edit_range/{ranges.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_range.html')

    def test_delete_ranges(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        response = self.client.get(f'/delete_range/{ranges.id}')
        self.assertRedirects(response, '/')
        existing_items = Range.objects.filter(id=ranges.id)
        self.assertEqual(len(existing_items), 0)

    def test_get_rolls(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        response = self.client.get(f'/get_rolls/{ranges.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rolls.html')

    def test_edit_rolls(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        rolls = Roll.objects.create(ranges=ranges, rolls='Test Roll', roll_width='4m', roll_size='25', location='A1')
        response = self.client.get(f'/edit_roll/{rolls.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_roll.html')

    def test_delete_rolls(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        rolls = Roll.objects.create(ranges=ranges, rolls='Test Roll', roll_width='4m', roll_size='25', location='A1')
        response = self.client.get(f'/delete_roll/{rolls.id}')
        self.assertRedirects(response, '/')
        existing_items = Roll.objects.filter(id=rolls.id)
        self.assertEqual(len(existing_items), 0)

    def test_get_cuts(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        rolls = Roll.objects.create(ranges=ranges, rolls='Test Roll', roll_width='4m', roll_size='25', location='A1')
        response = self.client.get(f'/getcuts/{rolls.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cut.html')

    def test_edit_cut(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        rolls = Roll.objects.create(ranges=ranges, rolls='Test Roll', roll_width='4m', roll_size='25', location='A1')
        cuts = Cut.objects.create(rolls=rolls, invoice='Test Invoice', cut_size='5')
        response = self.client.get(f'/edit_cut/{cuts.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_cut.html')

    def test_delete_cut(self):
        supplier = Supplier.objects.create(supplier='Test Supplier')
        ranges = Range.objects.create(supplier=supplier, ranges='Test Range')
        rolls = Roll.objects.create(ranges=ranges, rolls='Test Roll', roll_width='4m', roll_size='25', location='A1')
        cuts = Cut.objects.create(rolls=rolls, invoice='Test Invoice', cut_size='5')
        response = self.client.get(f'/delete_cut/{cuts.id}')
        self.assertRedirects(response, '/')
        existing_items = Cut.objects.filter(id=cuts.id)
        self.assertEqual(len(existing_items), 0)
