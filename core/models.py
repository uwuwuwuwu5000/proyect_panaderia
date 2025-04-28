from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from distutils.command.upload import upload
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name ='Id Producto')
    nomProducto = models.CharField(max_length=30,verbose_name='Producto')
    descProducto = models.CharField(max_length=550,verbose_name='Descripción')
    imagen = models.ImageField(upload_to="imagenes",null=True, verbose_name='Imagen')
    stock = models.IntegerField(verbose_name='stock', default=0,
                               validators=[
                                    MinValueValidator(0),
                                    MaxValueValidator(90000)
    ])
    precio= models.IntegerField(verbose_name='Precio',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(90000)
    ])
    
    def __str__(self):
        return self.nomProducto
    
class Cursos(models.Model):
       idCurso = models.IntegerField(primary_key=True,verbose_name='idCursos')
       nomCurso = models.CharField(max_length=50,verbose_name='nomCursos')
       descCurso = models.CharField(max_length=300, verbose_name='descCurso')
       precioCurso= models.IntegerField(validators=[MinValueValidator(1),
                                                    MaxValueValidator(999999)],
                                                    verbose_name='Precio')
       duracion = models.CharField(max_length=15,verbose_name='duracion')
       cupos = models.IntegerField(verbose_name='cupos')

       LOAN_HORARIO = (
            ('mt', 'Mañana 08:00 - 12:00 / Tarde 17:00 - 21:00'),
            ('ma', 'Mañana 08:00 - 12:00'),
            ('ta', 'Tarde 17:00 - 21:00'),
       )
       horario = models.CharField(max_length=2, choices = LOAN_HORARIO, default='mt')
       fechaInicio = models.DateField()
       fechaTermino = models.DateField(null=True,blank=True)
       img = models.ImageField(upload_to="imagenes",null=True,verbose_name='img')

       def __str__(self):
            return self.nomCurso


class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    LOAN_ESTADO = (
         ('RE', 'Recibido'),
         ('NR', 'No Recibido'),
         ('PP', 'Procesando Pedido'),
    )
    estado = models.CharField(max_length=2, choices = LOAN_ESTADO, default='RE')
    def __str__(self):
        return f'Boleta {self.id_boleta} - {self.user.username}'

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return f'{self.cantidad} x {self.id_producto.nomProducto} - Boleta {self.id_boleta.id_boleta}'



