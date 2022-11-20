from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F, ExpressionWrapper, IntegerField
from .models import Supplier, Range, Roll, Cut
from .forms import SupplierForm, RangeForm, RollForm, CutForm
from django.contrib import messages
from decimal import Decimal


# Create your views here.


def get_supplier(request):
    """
    Renders main page, with suppliers available
    """
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, "supplier.html", context)


def add_supplier(request):
    """
    Adds new supplier
    """
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Supplier Added.')
            form.save()
            return redirect('get_supplier')
    form = SupplierForm()
    context = {
        'form': form
    }
    return render(request, "add_supplier.html", context)


def edit_supplier(request, supplier_id):
    """
    Edit's existing suppliers and updates database with any changes
    """
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier Updated.')
            return redirect('get_supplier')
    form = SupplierForm(instance=supplier)
    context = {
        'form': form
    }
    return render(request, 'edit_supplier.html', context)


def delete_supplier(request, supplier_id):
    """
    Delete's selected supplier
    """
    supplier = get_object_or_404(Supplier, id=supplier_id)
    supplier.delete()
    messages.success(request, 'Supplier Deleted.')
    return redirect('get_supplier')


def get_ranges(request, supplier_id):
    """
    Returns relevant Ranges linked to the Supplier Id that is selected
    """
    supplier = get_object_or_404(Supplier, id=supplier_id)
    ranges = Range.objects.filter(supplier=supplier_id)
    context = {
        'ranges': ranges
    }
    return render(request, "ranges.html", context)


def add_range(request):
    """
    Creates new Range within Supplier
    """
    if request.method == "POST":
        form = RangeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Range Added.')
            return redirect('get_supplier')
    form = RangeForm()
    context = {
        'form': form
    }
    return render(request, "add_range.html", context)


def edit_range(request, range_id):
    """
    Edits existing Range, and updates database
    """
    ranges = get_object_or_404(Range, id=range_id)
    if request.method == "POST":
        form = RangeForm(request.POST, instance=ranges)
        if form.is_valid():
            form.save()
            messages.success(request, 'Range Edited.')
            return redirect('get_supplier')
    form = RangeForm(instance=ranges)
    context = {
        'form': form
    }
    return render(request, 'edit_range.html', context)


def delete_range(request, range_id):
    """
    Deletes Range from Database, and subsequent data linked with it
    """
    ranges = get_object_or_404(Range, id=range_id)
    ranges.delete()
    messages.success(request, 'Range Deleted.')
    return redirect('get_supplier')


def get_rolls(request, range_id):
    """
    Returns all Rolls linked with the selected Range Id in the database
    """
    ranges = get_object_or_404(Range, id=range_id)
    rolls = Roll.objects.filter(ranges=range_id)
    context = {
        'rolls': rolls
    }
    return render(request, "rolls.html", context)


def addroll(request):
    """
    Adds Roll to Database
    """
    if request.method == "POST":
        form = RollForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roll Added.')
            return redirect('get_supplier')
    form = RollForm()
    context = {
        'form': form
    }
    return render(request, "add_roll.html", context)


def edit_roll(request, roll_id):
    """
    Edits existing Roll, and updates the database
    """
    rolls = get_object_or_404(Roll, id=roll_id)
    if request.method == "POST":
        form = RollForm(request.POST, instance=rolls)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roll Updated.')
            return redirect('get_supplier')
    form = RollForm(instance=rolls)
    context = {
        'form': form
    }
    return render(request, 'edit_roll.html', context)


def delete_roll(request, roll_id):
    """
    Deletes selected Roll, and any linked data with it from the database
    """
    rolls = get_object_or_404(Roll, id=roll_id)
    rolls.delete()
    messages.success(request, 'Roll Deleted.')
    return redirect('get_supplier')


def getcuts(request, roll_id):
    """
    Returns cuts from the database linked to the Roll Id
    """
    rolls = get_object_or_404(Roll, id=roll_id)
    cuts = Cut.objects.filter(rolls=roll_id)
    total_cut = Cut.objects.values('cuts').annotate(Sum('cut_size'))
    total_roll = Roll.objects.values('rolls').annotate(Sum('roll_size'))
    roll = total_roll[0]['roll_size__sum']
    cut = total_cut[0]['cut_size__sum']
    balance = roll - cut
    context = {
        'cuts': cuts,
        'balance': balance
    }
    return render(request, 'cut.html', context)


def addcut(request):
    """
    Adds cut to the database
    """
    if request.method == "POST":
        form = CutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cut Added.')
            return redirect('get_supplier')
    form = CutForm()
    context = {
        'form': form
    }
    return render(request, "add_cut.html", context)


def edit_cut(request, cut_id):
    """
    Edits existing cut, and updates the database
    """
    cuts = get_object_or_404(Cut, id=cut_id)
    if request.method == "POST":
        form = CutForm(request.POST, instance=cuts)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cut Updated.')
            return redirect('get_supplier')
    form = CutForm(instance=cuts)
    context = {
        'form': form
    }
    return render(request, 'edit_cut.html', context)


def delete_cut(request, cut_id):
    """
    Deletes selected cut from the database
    """
    cuts = get_object_or_404(Cut, id=cut_id)
    cuts.delete()
    messages.success(request, 'Cut Deleted.')
    return redirect('get_supplier')


def toggle_cut(request, cut_id):
    """
    When button is clicked, updates database that the cut has been made,
    who made the cut, and date of cut
    """
    cuts = get_object_or_404(Cut, id=cut_id)
    cuts.cuts = not cuts.cuts
    cuts.cut_by = request.user
    cuts.save()
    messages.success(request, 'Cut has been marked!')
    return redirect('get_supplier')


def calc(request, roll_id):
    """
    Works out the remaining Roll Balance, taking the roll size
    and subtracting the total of the cut sizes linked to that
    roll. To be updated every time a new cut is added.
    """
    rolls = get_object_or_404(Roll, id=roll_id)
    cuts = Roll.objects.filter(rolls=roll_id)
    total_cut = Cut.objects.values('rolls_id').annotate(Sum('cut_size'))
    total_roll = Roll.objects.values('rolls').annotate(Sum('roll_size'))
    cut = total_cut[roll_id == 'rolls_id']['cut_size__sum']
    roll = total_roll[rolls == 'rolls']['roll_size__sum']
    balance = roll - cut
    rolls.roll_balance = balance
    rolls.save()
    messages.success(request, 'Roll Balance calculated!')
    return redirect('get_supplier')
