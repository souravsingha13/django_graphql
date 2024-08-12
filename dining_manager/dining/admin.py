from django.contrib import admin
from .models import Consumer, ProductCatagory, Products

class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  
    search_fields = ('name', 'email')  

class ProductCatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'catagory')  
    search_fields = ('name', 'catagory__name')  
    list_filter = ('catagory',)  

# Register the models with the custom admin classes
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(ProductCatagory, ProductCatagoryAdmin)
admin.site.register(Products, ProductsAdmin)
