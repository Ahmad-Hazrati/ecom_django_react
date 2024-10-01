from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'address', 'phone', 'created_at']
        
  
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'storeId', 'category', 'price', 'stock', 'condition', 'created_at']
              

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ['id', 'title', 'ulr']
        

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'userId', 'name', 'created_at']
        
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'userId', 'quantity']
        

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cartId', 'productId', 'quantity', 'created_at']
        

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['imgFile']
        

class JoinSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='productId')
    class Meta:
        model = CartItem
        fields = ['cartId', 'productId', 'quantity', 'product_details', 'created_at']
              