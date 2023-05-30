from django.contrib import admin
from store.models import Product, Category, Cart, Cart_Item, Saved_Item, Address


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
    
@admin.register( Cart_Item )
class Cart_ItemAdmin (admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_display_links = ('cart', 'product')
    
@admin.register( Saved_Item )
class Saved_ItemAdmin (admin.ModelAdmin):
    list_display = ('owner', 'product', 'added')
    list_display_links = ('owner', 'product')
    
@admin.register( Address )
class AddressAdmin (admin.ModelAdmin):
    list_display = ('customer','home_address_1','home_address_2', 'bus_stop', 'city')
    list_display_links = ('customer', 'city' )
    
