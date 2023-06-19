from django.contrib import admin
from .models import Element, Category, Type
# Register your models here.
@admin.register(Type, Category, Element)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    
    
class ElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    