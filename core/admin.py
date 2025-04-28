from django.contrib import admin
from .models import Producto, Cursos,Boleta,detalle_boleta 
# Register your models here.

admin.site.register(Producto)
admin.site.register(Cursos)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)