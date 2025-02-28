from django.shortcuts import render
from .models import ProductType,Product,Purchase,Department,Vendor,Sales,Customer
from rest_framework.viewsets import  ModelViewSet
from .serializers  import ProductTypeSerializer,ProductSerializer,PurchaseSerializer,DepartmentSerializer,VendorSerializer,SalesSerializer,CustomerSerializer,UserSerializer,GroupSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import DjangoModelPermissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group








# Create your views here.
@api_view(['GET'])
@permission_classes([])
def group(request):
    group_objs =  Group.objects.all()
    serializer =  GroupSerializer(group_objs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([])
def register(request):
    password  = request.data.get('password')
    hash_password = make_password(password)
    serializer =  UserSerializer(data=request.data)
    if  serializer.is_valid():
        a =  serializer.save()
        a.password = hash_password
        a.save()
        return Response("User created successfully")
    else:
        return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([])
def login (request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user ==  None:
        return Response("Invalid email or password")
    else:
        token ,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)


class  ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    filterset_fileds = ['department','type']
    search_fields  = ['name']

class ProductApiView(GenericAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes =  [DjangoModelPermissions]
    filterset_fileds = ['department','type']
    search_fields  = ['name']



    def get(self,request):
        products = Product.objects.all()
        products_filter = self.filter_queryset(products)
        serializer = ProductSerializer(products_filter,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Created")
        else:
            return Response(serializer.errors)

class ProductDetailApiView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fileds = ['department','type']
    search_fields  = ['name']
    
    def get(self,request,pk):
        try:
            product_obj = Product.objects.get(id=pk)
        except:
            return Response("Data Not Found")
        serializer  = ProductSerializer(product_obj)
        return Response(serializer.data)
    def  put(self,request,pk):
        try:
            product_obj = Product.objects.get(id=pk)
        except:
            return Response("Data Not Found")
        serializer = ProductSerializer(product_obj,data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response("Data Updated")
        else:
            return Response(serializer.errors)
    
    def delete(slef,request,pk):
        try:
            product_obj = Product.objects.get(id=pk)
        except:
            return Response("Data Not Found")
        product_obj.delete()
        return  Response("Data Deleted")




            
        
class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_fileds = ['department','type']
    search_fields  = ['name']
    
class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_fileds = ['department','type']
    search_fields  = ['name']
    
class VendorApiView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filterset_fileds = ['department','type']
    search_fields  = ['name']
    
class  SalesApiView(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filterset_fileds = ['department','type']
    search_fields  = ['name']

class CustomerApiView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fileds = ['department','type']
    search_fields  = ['name']
    
    

    
    
    

