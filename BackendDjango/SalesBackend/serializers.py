
from rest_framework import serializers
from SalesBackend.models import User, Product, Customer, Sales

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'username', 'password', 'privilege']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pro_id', 'pro_name', 'quantity', 'buy_price', 'sale_price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name', 'address', 'mobile']

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['sales_id', 'quantity', 'datetime', 'pay_status', 'user', 'product','customer']
