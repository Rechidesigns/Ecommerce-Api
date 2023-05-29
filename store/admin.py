from django.contrib import admin
from .models import Product, Category, Cart, Cartitem, SavedItem, Address


@admin.register( Category )
class CategoryAdmin (admin.ModelAdmin):
    list_display = ( 'title', 'slug', 'featured_product','icon' )
    list_display_links = ( 'title', 'slug' )

@admin.register( Product )
class ProductAdmin (admin.ModelAdmin):
    list_display = ('name','description', 'discount','image','old_price','category','slug','inventory','top_deal','flash_sales',)
    list_display_links = ('name' , 'description' )

@admin.register( Cart )
class CartAdmin (admin.ModelAdmin):
    list_display = ( 'owner', 'created', 'completed', 'session_id' )
    list_display_links = ( 'owner', 'created' )
    
@admin.register( Cartitem )
class CartitemAdmin (admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_display_links = ('cart', 'product')
    
@admin.register( SavedItem )
class SavedItemAdmin (admin.ModelAdmin):
    list_display = ('owner', 'product', 'added')
    list_display_links = ('owner', 'product')
    
@admin.register( Address )
class AddressAdmin (admin.ModelAdmin):
    list_display = ('customer','home_address_1','home_address_2', 'bus_stop', 'city')
    list_display_links = ('customer', 'city' )
    
