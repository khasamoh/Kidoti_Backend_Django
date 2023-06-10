from django.db import models

# Create your models here.
# models.py

from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    privilege = models.CharField(max_length=255)

    def __str__(self):
        return self.user_id
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_id

class Product(models.Model):
    pro_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    buy_price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)

    def __str__(self):
        return self.Pro_id
    

class Sales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now=True)
    pay_status = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fkUser')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='fkproduct')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='fkcustomer')

    def __str__(self):
        return self.sales_id
