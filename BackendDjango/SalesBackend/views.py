from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from SalesBackend.models import User,Product,Customer,Sales
from .serializers import UserSerializer, ProductSerializer, SalesSerializer, CustomerSerializer

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
            'pro_name': sale.product.pro_name,
            'sale_price': sale.product.sale_price,
            'buy_price': sale.product.buy_price,
            'quantity': sale.quantity,
            # ... other fields you want to include
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