#from django.shortcuts import render
#Create your views here

from rest_framework.decorators import api_view
from rest_framework.response import Response
from SalesBackend.models import User,Product,Customer,Sales
from .serializers import UserSerializer, ProductSerializer, SalesSerializer, CustomerSerializer

# Start API for User
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# End API for User

# Start API for Product
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# End API for Product

# Start API for Customer
@api_view(['GET'])
def customer_list(request):
    customers = Product.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def customer_create(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# End API for Customer

# Start API for Sales
@api_view(['GET'])
def sale_list(request):
    sales = Sales.objects.all()
    serializer = SalesSerializer(sales, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def sale_create(request):
    serializer = SalesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
# End API for Sales