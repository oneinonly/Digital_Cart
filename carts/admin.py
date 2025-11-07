from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','cart_id', 'date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'quantity', 'is_active')

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)

