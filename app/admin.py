from django.contrib import admin

from .models import Category,SubCategory, Product, contact_us, Order, Brand
# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(contact_us)
admin.site.register(Order)
admin.site.register(Brand)