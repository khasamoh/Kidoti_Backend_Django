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

# @api_view(['PUT'])
# def update_product(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response({'error': 'Product not found'}, status=404)
    
#     if request.method == 'PUT':
#         pro_name = request.data.get('pro_name')
#         quantity = request.data.get('quantity')
#         buy_price = request.data.get('buy_price')
#         sale_price = request.data.get('sale_price')

#         # Update the product fields
#         product.pro_name = pro_name
#         product.quantity = quantity
#         product.buy_price = buy_price
#         product.sale_price = sale_price
#         product.save()

#         return Response({'message': 'Product updated successfully'})
#     else:
#         return Response({'error': 'Invalid request method'}, status=400)

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