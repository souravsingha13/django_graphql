from django.contrib import admin
from .models import Consumer, ProductCatagory, Products,Expenses,Meal

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

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price', 'buyer')
    search_fields = ('product__product_name', 'buyer__name')
    list_filter = ('product', 'buyer')


class MealAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'meal_date', 'meal_count')
    search_fields = ('consumer__name', 'meal_date')
    list_filter = ('meal_date',)




# Register the models with the custom admin classes
admin.site.register(Meal, MealAdmin)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(ProductCatagory, ProductCatagoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Expenses, ExpensesAdmin)
