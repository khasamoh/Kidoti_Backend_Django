from django.urls import path
from .views import user_list, user_create, product_list, product_create, customer_list, customer_create, sale_list, sale_create

urlpatterns = [
    #user
    path('users/', user_list, name='user-list'),
    path('users/create/', user_create, name='user-create'),
    
    #Product
    path('products/', product_list, name='product-list'),
    path('products/create/', product_create, name='product-create'),
    
    #Customer
    path('customers/', customer_list, name='customer-list'),
    path('customers/create/', customer_create, name='customer-create'),
    
    #Sales
    path('sales/', sale_list, name='sale-list'),
    path('sales/create/', sale_create, name='sale-create'),
]
