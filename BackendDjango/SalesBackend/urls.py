from django.urls import path

from .views import login,user_list, user_create, get_sold_product,product_list,product_list_byId,customer_list_byId,user_list_byId,delete_user,delete_customer,delete_sale, delete_product, product_create, customer_list, customer_create, update_product, sale_create

urlpatterns = [
    path('login/', login, name='login'),
    #user
    path('users/', user_list, name='user-list'),
    path('users/<int:user_id>/', user_list_byId, name='user_list_byId'),
    path('users/create/', user_create, name='user-create'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),
    
    #Product
    path('products/', product_list, name='product-list'),
    path('products/<int:pro_id>/', product_list_byId, name='product-list-byId'),
    path('products/create/', product_create, name='product-create'),
    path('products/delete/<int:pro_id>/', delete_product, name='delete_product'),
    #ToDO===>
    path('products/update/<int:pro_id>/', update_product, name='update_product'),

    #Customer
    path('customers/', customer_list, name='customer-list'),
    path('customers/<int:customer_id>/', customer_list_byId, name='customer_list_byId'),
    path('customers/create/', customer_create, name='customer-create'),
    path('customers/delete/<int:customer_id>/', delete_customer, name='delete_customer'),
    
    #Sales
    path('sales/', get_sold_product, name='sale-list'),
    path('sales/create/', sale_create, name='sale-create'),
    path('sales/delete/<int:sales_id>/', delete_sale, name='delete_sale'),
    
]
