from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('c_id', 'c_code', 'c_name', 'i_code', 'i_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'c_id', 'p_name', 'img_src', 'price', 'link')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
