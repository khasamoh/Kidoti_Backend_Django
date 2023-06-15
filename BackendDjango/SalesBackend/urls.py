from django.urls import path
from .views import user_list, user_create, product_list,product_list_byId , delete_product, product_create, customer_list, customer_create, update_product, sale_list, sale_create

urlpatterns = [
    #user
    path('users/', user_list, name='user-list'),
    path('users/create/', user_create, name='user-create'),
    
    #Product
    path('products/', product_list, name='product-list'),
    path('products/<int:pro_id>/', product_list_byId, name='product-list-byId'),
    path('products/create/', product_create, name='product-create'),
    path('products/delete/<int:pro_id>/', delete_product, name='delete_product'),
    #ToDO===>
    path('products/update/<int:pro_id>/', update_product, name='update_product'),
    
    
    #Customer
    path('customers/', customer_list, name='customer-list'),
    path('customers/create/', customer_create, name='customer-create'),
    
    #Sales
    path('sales/', sale_list, name='sale-list'),
    path('sales/create/', sale_create, name='sale-create'),
]
