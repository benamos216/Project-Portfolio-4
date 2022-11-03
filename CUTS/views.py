from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier
from .forms import SupplierForm

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
