from django.shortcuts import render
from .models import Supplier

# Create your views here.


def get_supplier(request):
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers
    }
    return render(request, "supplier.html", context)
