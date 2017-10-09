from .models import Producto, Venta, Categoria, UnidadMed, Cliente, ShoppingCart
from rest_framework import serializers, viewsets


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class VentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venta
        fields = '__all__'


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class UnidadMedSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnidadMed
        fields = '__all__'


class UnidadMedViewSet(viewsets.ModelViewSet):
    queryset = UnidadMed.objects.all()
    serializer_class = UnidadMedSerializer


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ShoppingCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
