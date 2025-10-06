from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('id', 'category_name', 'slug', 'description', 'cat_image')
admin.site.register(Category, CategoryAdmin)
    