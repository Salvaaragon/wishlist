from django.contrib import admin
from product_list.models import Product, ProductType, ProductList

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(ProductList)