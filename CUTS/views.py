from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier, Range, Roll, Cut
from .forms import SupplierForm, RangeForm, RollForm, CutForm

# Create your views here.


def get_supplier(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, "supplier.html", context)


def add_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = SupplierForm()
    context = {
        'form': form
    }
    return render(request, "add_supplier.html", context)


def edit_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = SupplierForm(instance=supplier)
    context = {
        'form': form
    }
    return render(request, 'edit_supplier.html', context)


def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    supplier.delete()
    return redirect('get_supplier')


def get_ranges(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    ranges = Range.objects.filter(supplier=supplier_id)
    context = {
        'ranges': ranges
    }
    return render(request, "ranges.html", context)


def add_range(request):
    if request.method == "POST":
        form = RangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = RangeForm()
    context = {
        'form': form
    }
    return render(request, "add_range.html", context)


def edit_range(request, range_id):
    ranges = get_object_or_404(Range, id=range_id)
    if request.method == "POST":
        form = RangeForm(request.POST, instance=ranges)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = RangeForm(instance=ranges)
    context = {
        'form': form
    }
    return render(request, 'edit_range.html', context)


def delete_range(request, range_id):
    ranges = get_object_or_404(Range, id=range_id)
    ranges.delete()
    return redirect('get_supplier')


def get_rolls(request, range_id):
    ranges = get_object_or_404(Range, id=range_id)
    rolls = Roll.objects.filter(ranges=range_id)
    context = {
        'rolls': rolls
    }
    return render(request, "rolls.html", context)


def addroll(request):
    if request.method == "POST":
        form = RollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = RollForm()
    context = {
        'form': form
    }
    return render(request, "add_roll.html", context)


def edit_roll(request, roll_id):
    rolls = get_object_or_404(Roll, id=roll_id)
    if request.method == "POST":
        form = RollForm(request.POST, instance=rolls)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = RollForm(instance=rolls)
    context = {
        'form': form
    }
    return render(request, 'edit_roll.html', context)


def delete_roll(request, roll_id):
    rolls = get_object_or_404(Roll, id=roll_id)
    rolls.delete()
    return redirect('get_supplier')


def getcuts(request, roll_id):
    rolls = get_object_or_404(Roll, id=roll_id)
    cuts = Cut.objects.filter(rolls=roll_id)
    context = {
        'cuts': cuts
    }
    return render(request, 'cut.html', context)


def addcut(request):
    if request.method == "POST":
        form = CutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = CutForm()
    context = {
        'form': form
    }
    return render(request, "add_cut.html", context)
