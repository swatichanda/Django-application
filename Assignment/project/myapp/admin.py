from django.contrib import admin
from .models import Invoice,InvoiceDetail
# Register your models here.

#@admin.register(Invoice)
#class InvoiceAdmin(admin.ModelAdmin):
 #   list_display = ['id', 'name', 'roll', 'city']
#from .models import Product, Contact,Orders,OrderUpdate
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
