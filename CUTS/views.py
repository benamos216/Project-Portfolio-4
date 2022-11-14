from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F, ExpressionWrapper
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
    rolls.roll_balance = Roll.objects.annotate(total_balance=F('roll_size')-F('Cut__cut_size'))
    rolls.save()
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


def update_cut_by(request):
    form = CutForm(request.POST)
    if form.is_valid():
        cut = form.save(commit=False)
        cut.cut_by = request.user
        cut.save()
    return render(request, 'cut.html')


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


def edit_cut(request, cut_id):
    cuts = get_object_or_404(Cut, id=cut_id)
    if request.method == "POST":
        form = CutForm(request.POST, instance=cuts)
        if form.is_valid():
            form.save()
            return redirect('get_supplier')
    form = CutForm(instance=cuts)
    context = {
        'form': form
    }
    return render(request, 'edit_cut.html', context)


def delete_cut(request, cut_id):
    cuts = get_object_or_404(Cut, id=cut_id)
    cuts.delete()
    return redirect('get_supplier')


def toggle_cut(request, cut_id):
    cuts = get_object_or_404(Cut, id=cut_id)
    cuts.cuts = not cuts.cuts
    cuts.cut_by = request.user
    cuts.save()
    return redirect('get_supplier')
