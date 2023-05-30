# Imports
import uuid
# Django import 
from django.db import models
from django.utils.translation import gettext_lazy as _

# Custom Apps 
from helpers.common.basemodel import BaseModel
from ecommerce.users.models import User



class Category( BaseModel ):
    
    title = models.CharField(
        max_length=200,
        blank= True,
        verbose_name= _("Category Title"),
        help_text= _("This holds the name of the category")
        )
    
    slug = models.SlugField(
        default= None,
        verbose_name= _("Slug"),
        help_text= _("This is the slug of the category")
        )
    
    featured_product = models.OneToOneField(
        'Product', on_delete=models.CASCADE, 
        blank=True, null=True, 
        related_name='featured_product',
        help_text= _("This is the product in which the category is featured")
        )
    
    icon = models.CharField(
        max_length=100, 
        default=None, 
        blank = True, 
        null=True,
        verbose_name= _("Icon"),
        help_text= _("This is the icon of the category")
        )

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    

class Product( BaseModel ):
    
    name = models.CharField(
        max_length=200,
        blank= True,
        verbose_name= _("Product Name"),
        help_text= _("This is the name of the product")
        )
    
    description = models.TextField(
        blank=True, 
        null=True,
        verbose_name= _("Description"),
        help_text= _("This is a short description of the product")
        )
    
    discount = models.BooleanField(
        default=False,
        verbose_name= _("Discount"),
        help_text= _("This holds if the product has a discount on it")
        )
    
    image = models.ImageField(
        verbose_name = _('Product Image'),
        upload_to = "photos/product_image",
        null =True,
        blank=True,
        help_text= _('Product  image for the current product, which should be in PNG, JPEG, or JPG format')
        )
    
    old_price = models.FloatField(
        default=100.00,
        verbose_name= _("Old Price"),
        help_text= _("This holds the old price of the product")
        )
    
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        blank=True, null=True, 
        related_name='products',
        help_text= _("This holds the Category the product belongs")
        )
    
    slug = models.SlugField(
        default=None,
        verbose_name= _("Slug"),
        help_text= _("This is the slug of the product")
        )
    
    inventory = models.IntegerField(
        default=5,
        verbose_name= _("Inventory"),
        help_text= _("This is the number of products in the inventory")
        )
    
    top_deal=models.BooleanField(
        default=False,
        verbose_name= _("Top Deal"),
        help_text= _("This indicates if the product is a top deal or not")
        )
    
    flash_sales = models.BooleanField(
        default=False,
        verbose_name= _("Flash Sales"),
        help_text= _("This indicates if the product ison flash sales or not")
        )
    

    # @property
    # def price(self):
    #     if self.discount:
    #         new_price = self.old_price - ((30/100)*self.old_price)
    #     else:
    #         new_price = self.old_price
    #     return new_price
    
    # # @property
    # def img(self):
    #     if self.image == "":
    #         self.image = ""
        
    #     return self.image

    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = _("Products ")
        verbose_name_plural = _("Products")
    
    

class Cart( BaseModel ):
    
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null = True, blank=True,
        verbose_name= _("Owner"),
        help_text= _("This is the customer that owns the cart")
    )
    
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name= _("Date Created"),
        help_text= _("This holds the date the cart was created")
        )
    
    completed = models.BooleanField(
        default=False,
        verbose_name= _("Date Completed"),
        help_text= _("This indicates if the cart is completed")
        )
    
    session_id = models.CharField(
        max_length=100,
        blank= True,
        null = True,
        verbose_name= _("Session ID"),
        help_text= _("This holds the session ID")
        )
    

    # @property
    # def num_of_items(self):
    #     cartitems = self.cartitems_set.all()
    #     qtysum = sum([ qty.quantity for qty in cartitems])
    #     return qtysum
    
    # @property
    # def cart_total(self):
    #     cartitems = self.cartitems_set.all()
    #     qtysum = sum([ qty.subTotal for qty in cartitems])
    #     return qtysum

    def __str__(self):
        return str(self.cart_id)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")



class Cart_Item ( models.Model ):
    
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, 
        blank=True, null=True,
        verbose_name= _("Cart"),
        help_text= _("This holds the cart items Id")
        )
    
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        related_name='cartitems',
        help_text= _("This holds the cart products")
        )
    
    quantity = models.IntegerField(
        default=0,
        verbose_name= _("Quantity"),
        help_text= _("This holds the cart quantity")
        )
    
    
    # @property
    # def subTotal(self):
    #     total = self.quantity * self.product.price
        
    #     return total
    
    def __str__(self):
        return str(self.quantity)
    
    
    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
    
   

class Saved_Item( BaseModel ):
    
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null = True, blank=True,
        verbose_name= _("Owner"),
        help_text= _("This holds the saved product")
        )
    
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        blank=True, null=True,
        verbose_name= _("Product"),
        help_text= _("This holds the saved product")
        )
    
    added = models.IntegerField(
        default=0,
        verbose_name= _("Added"),
        help_text= _("This holds the the numbers of added items")
        )
    
    
    
    def __str__(self):
        return str(self.id)
    
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = _("Saved Item")
        verbose_name_plural = _("Saved Items")
    
    
class Address( BaseModel ):
    
    customer = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        default='',
        related_name= _("customer"),
        help_text= _("This holds the customer details of the address")
        )
    
    home_address_1 = models.CharField(
        max_length=250,
        verbose_name= _("Home Address 1"),
        help_text= _("This holds the customers address the product will be delivered to")
        )
    
    home_address_2 = models.CharField(
        max_length=250,
        verbose_name= _("Home Address 2"),
        help_text= _("This holds the customers address the product will be delivered to")
        )
    
    
    bus_stop = models.CharField(
        max_length=100,
        null= True,
        blank = True,
        verbose_name= _("Bus Stop"),
        help_text= _("This holds the bus stop the product will be delivered to")
        )
    
    city = models.CharField(
        max_length=100,
        verbose_name= _("City"),
        help_text= _("This holds the city the product will be delivered to")
        )
    
    state = models.CharField(
        max_length=20,
        verbose_name= _("State"),
        help_text= _("This holds the state the product will be delivered to")
        )
    
    # def __str__(self):
    #     return self.home_address
    
    
    # def __str__(self):
    #     return f"{self.home_address_1} {self.home_address_2}"
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.customer})"
    
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")