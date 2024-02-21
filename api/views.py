from rest_framework import viewsets, permissions
from api.models import *
from api.serializers import *
from rest_framework import status,views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate, login 
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters, status

class ProductoViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter, )
    search_fields = ['productoName', 'productoPrice']
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]
    

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer



class ProductoPopularViewSet(viewsets.ModelViewSet):
    queryset = ProductoPopular.objects.all()
    serializer_class = ProductoPopularSerializer
    permission_classes = [permissions.AllowAny]

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    
class TiendaApiView(generics.ListCreateAPIView):
    search_fields = ['productoName']
    filter_backends = (filters.SearchFilter,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TiendaCATApiView(generics.ListCreateAPIView):
    search_fields = ['productoCategoria']
    filter_backends = (filters.SearchFilter,)
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class JefeViewSet(viewsets.ModelViewSet):
    queryset = Jefe.objects.all()
    serializer_class = JefeSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]

class ComercViewSet(viewsets.ModelViewSet):
    queryset = Comercializadora.objects.all()
    serializer_class = ComercSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [authentication.BasicAuthentication]


class ProductoSearch(generics.ListAPIView):
    
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        categoria_id = request.query_params.get('categoria_id')
        if categoria_id:
            return queryset.filter(productoCategoria__id=categoria_id)
        return queryset
    
class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [CategoriaFilter]

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer



