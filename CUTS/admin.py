from django.contrib import admin
from .models import Supplier, Range, Roll, Cut

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Range)
admin.site.register(Roll)
admin.site.register(Cut)
