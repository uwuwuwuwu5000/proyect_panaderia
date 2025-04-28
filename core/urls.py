from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',views.index, name='index'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('productos/',views.productos,name='productos'),
    path('cursos/',views.cursos,name='cursos'),
    path('crear/',views.crear,name='crear'),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminarP/<id>/', views.eliminar, name="eliminarP"),
    path('logout/', views.cerrar, name="cerrar"),
    path('registrar/', views.registrar, name="registrar"),
    path('perfil/', views.detallePerfil, name="perfil"),
    path('modPerfil/', views.modPerfil,name="modPerfil"),
    path('crearCurso/', views.crearCurso, name="crearCurso"),
    path('modificarCurso/<id>/', views.modificarCurso, name="modificarCurso"),
    path('eliminarCurso/<id>/', views.eliminarCurso, name="eliminarCurso"),
    path('tienda/',views.tienda, name="tienda"),
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar/<id>', views.eliminar_producto, name="eliminar"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),
    path('buscar/', views.buscar, name='buscar'),
    path('historialCompras/',views.historial_compras, name='historial'),
]