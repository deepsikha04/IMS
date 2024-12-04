from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Sell)
admin.site.register(Customers)
admin.site.register(Supplier)
admin.site.register(Department)
