from rest_framework import serializers
from api.models import *
from rest_framework.authtoken.models import Token
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    


class ProductoPopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoPopular
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'
        
    def create(self, validated_data):
        cantidad = validated_data['cantidad']
        preciounitario = validated_data['preciounitario']

        # Calcula el subtotal
        subtotal = cantidad * preciounitario

        # Agrega el subtotal a los datos validados
        validated_data['subtotal'] = subtotal

        # Llama al método create de la clase base para realizar la creación
        return super().create(validated_data)
    
class CarritoTotalSerializer(serializers.Serializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2)

    def to_representation(self, instance):
        return {'total': instance['total']}
    
class JefeSerializer(serializers.Serializer):
    class Meta:
        model = Jefe
        fields = "__all__"

class ComercSerializer(serializers.Serializer):
    class Meta:
        model = Comercializadora
        fields = "__all__"

class ProductoCatSerializer(serializers.Serializer):
    class Meta:
        model = Producto
        fields = "__all__"

class FacturaSerializer(serializers.Serializer):
    class Meta:
        model = Factura
        fields = "__all__"
  
