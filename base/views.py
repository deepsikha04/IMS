from django.shortcuts import render
from .models import ProductType, Product, Purchase, Sell, Customers, Supplier, Department
from rest_framework.viewsets import ModelViewSet    
from .serializer import ProductTypeSerializer, ProductSerializer, PurchaseSerializer, SellSerializer, CustomersSerializer, SupplierSerializer, DepartmentSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

# Create your views here.

class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SellViewSet(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class CustomersViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')


    user = authenticate(username=email, password=password)

    if user == None:
        return Response('Invalid credentials')
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)
        

@api_view(['POST'])

def register(request):
    password = request.data.get('password')
    hash_password = make_password(password) 
    request.data['password'] = hash_password
    serializer = UserSerializer(data=request.data)
    if serializer .is_valid():
        serializer.save()
        return Response('Data created!')
    else:
        return Response(serializer.errors)
    











   

      






