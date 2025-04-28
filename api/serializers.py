from rest_framework import serializers as s
from django.contrib.auth.models import User
from core.models import Producto

class UserSerializer(s.Serializer):
    id = s.ReadOnlyField()
    first_name = s.CharField()
    last_name = s.CharField()
    username = s.CharField()
    email = s.CharField()
    password = s.CharField()

    def create(self, data):
        user = User()
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.username = data.get('username')
        user.email = data.get('email')
        user.set_password(data.get('password'))
        user.save()
        return user
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users)!=0:
            raise s.ValidationError("El usuario ya existe, ingrese otro usuario")
        else:
            return data

# class ProductSerializer(s.Serializer):
#     idProducto = s.IntegerField()
#     nomProducto = s.CharField()
#     descProducto = s.CharField()
#     imagen = s.ImageField()
#     stock = s.IntegerField()
#     precio = s.IntegerField()

#     def create(self, data):
#         producto = Producto()
#         producto.idProducto = data.get('idProducto')    
#         producto.nomProducto = data.get('nomProducto')    
#         producto.descProducto = data.get('descProducto')    
#         producto.imagen = data.get('imagen')    
#         producto.stock = data.get('stock')    
#         producto.precio = data.get('precio')
#         producto.saver()
#         return producto

#     def validate_producto(self, data):
#         productos = Producto.objects.filter(idProducto = data)
#         if len(productos)!=0:
#             raise s.ValidationError('La ID del producto debe ser distinta') 
#         else:
#             return data 

class ProductoSerializer(s.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nomProducto', 'descProducto', 'imagen', 'stock', 'precio'] 