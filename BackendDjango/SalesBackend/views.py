from datetime import datetime, date
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from SalesBackend.models import User,Product,Customer,Sales
from .serializers import UserSerializer, ProductSerializer, SalesSerializer, CustomerSerializer

current_date = datetime.now().date()
formatted_date = current_date.strftime('%B %d, %Y')
#Login
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)

    if user.check_password(password, user.password):
        if user.is_verified:
            userid = user.user_id
            return Response({
                'message': 'Valid login',
                'user_id': userid
            })
        else:
            return Response({
                'message': 'User not valid'
            })
    else:
        return Response({'message': 'Invalid credentials'}, status=401)
        
# Start API for User
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_list_byId(request,user_id):
    user = User.objects.get(user_id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_user(request, user_id):
    user = User.objects.get(user_id=user_id)
    user.delete()
    return Response(status=204)

# class UserSerializers(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# End API for User

# Start API for Product
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_list_byId(request,pro_id):
    product = Product.objects.get(pro_id=pro_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_product(request, pro_id):
    product = Product.objects.get(pro_id=pro_id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_product(request, pro_id):
    product = Product.objects.get(pro_id=pro_id)
    product.delete()
    return Response(status=204)
# End API for Product

# Start API for Customer
@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customer_list_byId(request,customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data)

@api_view(['POST'])
def customer_create(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_customer(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    customer.delete()
    return Response(status=204)

# End API for Customer

# Start API for Sales
@api_view(['GET'])
def get_sold_product(request):
    sales = Sales.objects.select_related('product')
    sold_data = [
        {
            'sales_id': sale.sales_id,
            'pro_name': sale.product.pro_name,
            'sale_price': sale.product.sale_price,
            'buy_price': sale.product.buy_price,
            'datetime': sale.datetime,
            'quantity': sale.quantity,
        }
        for sale in sales
    ]
    return JsonResponse({'sold_data': sold_data})

@api_view(['GET'])
def get_todaysold_product(request):
    today = date.today()
    sales = Sales.objects.filter(datetime__date=today).select_related('product')
    
    sold_data = [
        {
            'sales_id': sale.sales_id,
            'pro_name': sale.product.pro_name,
            'sale_price': sale.product.sale_price,
            'buy_price': sale.product.buy_price,
            'datetime': sale.datetime,
            'quantity': sale.quantity,
        }
        for sale in sales
    ]
    
    return JsonResponse({'sold_data': sold_data})

@api_view(['POST'])
def sale_create(request):
    serializer = SalesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_sale(request, sales_id):
    sales = Sales.objects.get(sales_id=sales_id)
    sales.delete()
    return Response(status=204)
# End API for Sales

#Count
@api_view(['GET'])
def user_count(request):
    num_rows = User.objects.count()
    return Response({'num_rows': num_rows})

@api_view(['GET'])
def product_count(request):
    num_rows = Product.objects.count()
    return Response({'num_rows': num_rows})

@api_view(['GET'])
def customer_count(request):
    num_rows = Customer.objects.count()
    return Response({'num_rows': num_rows})

@api_view(['GET'])
def total_todaysold_product(request):
    today = date.today()
    sales = Sales.objects.filter(datetime__date=today).select_related('product')
    total_sales = 0
    Total_Sales = [
        {
            'sale_price': sale.product.sale_price,
            'quantity': sale.quantity,
            'total': sale.quantity * sale.product.sale_price,
        }
        for sale in sales
    ]
    
    for sale_data in Total_Sales:
        total_sales += sale_data['total'] 
    
    return JsonResponse({'TotalSales': Total_Sales, 'TotalSalesAmount': total_sales})
