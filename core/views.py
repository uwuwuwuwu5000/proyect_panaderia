from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Cursos, Boleta,detalle_boleta
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import ProductoForm, RegistroUserForm,CursoForm, UserUpdateForm
from .compras import Carrito
from django.contrib import messages

# Create your views here.

def admin_test(user):
    return user.is_authenticated and user.is_staff

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def productos(request): 
    panes_list = Producto.objects.all()
    paginator = Paginator(panes_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productos.html', {'page_obj': page_obj})

def cursos(request):
    cursos = Cursos.objects.all()
    return render(request,'cursos.html', {'cursos':cursos})


@user_passes_test(admin_test)
@login_required
def crear(request):
    if request.method=='POST':
        prodform = ProductoForm(request.POST, request.FILES)
        if prodform.is_valid():
            prodform.save()
            return redirect('productos')
    else:
        prodform=ProductoForm()
    return render(request,'crear.html', {'prodform':prodform})

@user_passes_test(admin_test)
@login_required
def eliminar(request, id):
    pan = get_object_or_404(Producto, idProducto=id)
    if request.method=='POST':
        if 'elimina' in request.POST:       
            pan.delete()               
            return redirect ('productos')
        else:
            return redirect('productos')
    return render(request, 'eliminar.html', {'pan': pan})

@user_passes_test(admin_test)
@login_required
def modificar(request, id):
    pan = Producto.objects.get(idProducto=id)
    datos={
        'forModificar': ProductoForm(instance=pan), 
        'pan': pan
    }
    if request.method=='POST':
        formulario=ProductoForm(request.POST, request.FILES, instance=pan)
        if formulario.is_valid():
            formulario.save()           #actualiza un objeto una vez que lo encuentra
            return redirect('productos')
    return render(request, 'modificar.html', datos)

def cerrar(request):
    logout(request)
    return redirect('index')


def registrar(request):
    data={
        'form': RegistroUserForm()
    }
    if request.method=='POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                    password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('index')
        data["form"]=formulario
    return render(request, 'registration/registrar.html',data)

@login_required
def detallePerfil(request):
    return render(request, 'detallePerfil.html')

@login_required
def modPerfil(request):
    user = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Actualizar y redirigir.
    else:
        form = UserUpdateForm(instance=user)  # Prellenar el formulario con los datos del usuario actual
    data = {
        'form': form,
    }
    return render(request, 'modPerfil.html', data)

# CRUD Cursos
@user_passes_test(admin_test)
@login_required
def crearCurso(request):
    if request.method=='POST':
        curForm = CursoForm(request.POST, request.FILES)
        if curForm.is_valid():
            curForm.save()         #similar en función al insert into
            return redirect ('cursos')
    else:
        curForm=CursoForm()
    return render(request, 'crearCurso.html',{'curForm':CursoForm})

@user_passes_test(admin_test)
@login_required
def modificarCurso(request, id):
    curso = Cursos.objects.get(idCurso=id)
    datos={
        'formModificar': CursoForm(instance=curso), #crea un objeto de tipo formulario
        'curso': curso,
    }
    if request.method=='POST':
        formulario=CursoForm(request.POST, request.FILES, instance=curso)
        if formulario.is_valid():
            formulario.save()          
            return redirect('cursos')
    return render(request, 'modificarCurso.html', datos)

@user_passes_test(admin_test)
@login_required
def eliminarCurso(request, id):
    curso = get_object_or_404(Cursos, idCurso=id)
    if request.method=='POST':
        if 'elimina' in request.POST:  
            curso.delete()               
            return redirect ('cursos')
        else:
            return redirect('cursos', idCurso=id)
    return render(request, 'eliminarCurso.html', {'curso': curso})

#Carrito
def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    if producto.stock > 0:
        carrito_compra.agregar(producto=producto)
        messages.success(request, "Producto añadido al carrito.")
    else:
        messages.error(request, "No hay suficiente stock para añadir este producto.")
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    

@login_required
def tienda(request):
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tienda.html', {'page_obj': page_obj})

def generarBoleta(request):
    precio_total=0
    productos = []

    #Validar stock antes de proceder
    for key, value in request.session['carrito'].items():
        producto = Producto.objects.get(idProducto=value['producto_id'])
        if producto.stock < value['cantidad']:
            messages.error(request, f"No hay suficiente stock para {producto.nomProducto}.")
            return redirect('tienda')

    # Calcular precio total y crear boleta
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total,user=request.user)
    boleta.save()

    #Crear detalles de la boleta y reducir stock
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(idProducto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            producto.stock -= cant
            producto.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total,
        'estado': boleta.get_estado_display
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)

def buscar(request):
    query = request.GET.get('q')
    if query:
        resultados = Producto.objects.filter(nomProducto__icontains=query)
    else:
        resultados = Producto.objects.all()
    
    datos = {
        'resultados': resultados,
        'query': query,
    }
    return render(request, 'busqueda.html', datos)

@user_passes_test(admin_test)
@login_required
def historial_compras(request):
    compras_list = Boleta.objects.all().prefetch_related('detalle_boleta_set__id_producto')
    paginator = Paginator(compras_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'histCompras.html', {'page_obj': page_obj})



