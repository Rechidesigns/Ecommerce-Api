from rest_framework import serializers
from store.models import Product

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'old_price', 'category','inventory', 'slug',]