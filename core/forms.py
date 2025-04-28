from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Cursos

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super(UserUpdateForm, self).save(commit=False)
        password1 = self.cleaned_data.get('password1')
        if password1:
            user.set_password(password1)
        if commit:
            user.save()
        return user


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto','nomProducto','descProducto','imagen','precio','stock']
        labels = {
            'idProducto': 'Id Producto',
            'nomProducto': 'Nombre Producto',
            'descProducto': 'Descripción Producto',
            'imagen': 'Imagen',
            'precio': 'Precio',
            'stock':'Stock'
        }
        widgets = {
            'idProducto': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese id producto',
                    'id': 'idproducto'
                }
            ),
            'nomProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre de producto',
                    'id': 'nomPro'
                }
            ),
            'descProducto': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripción del producto',
                    'id': 'descPro',
                    'rows': 3
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio del producto',
                    'id': 'precio'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock',
                    'id': 'stock'
                }
            )
        }

class CursoForm(forms.ModelForm):
    class Meta: 
        model = Cursos
        fields =  ['idCurso','nomCurso','descCurso','precioCurso','duracion','cupos','horario','fechaInicio','fechaTermino','img']
        labels = {
            'idCurso': 'Id Curso',
            'nomCurso': 'Nombre Curso:',
            'descCurso': 'Descripcion',
            'precioCurso': 'Precio',
            'duracion': 'Duracion',
            'cupos': 'Cupos',
            'horario': 'Horario',
            'fechaInicio': 'Fecha inicio',
            'fechaTermino': 'Fecha termino',
            'img': 'Imagen',
        }
        widgets = {
            'idCurso': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Id Curso',
                    'id': 'idcurso',
                }
            ),
            'nomCurso': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre del Curso',
                    'id': 'nomCur'
                }
            ),
            'descCurso': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion del Curso',
                    'rows':'4',
                    'id': 'descCur'
                }
            ),
            'precioCurso': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese precio del curso',
                    'id': 'precioCur'
                }
            ),
            'duracion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese duracion',
                    'id': 'duracionCurso'
                }
            ),
            'cupos': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese cantidad de cupos',
                    'id': 'Cupos'
                }
            ),
            'horario': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese horario disponible',
                    'id': 'Horario'
                }
            ),
            'fechaInicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de inicio',
                    'id': 'fechIni',
                    'type':'date',
                    'onkeydown': 'return false;' 
                    
                }
            ),
            'fechaTermino': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de termino',
                    'id': 'fechTermino',
                    'type':'date',
                    'onkeydown': 'return false;' 
                }
            ),
            'img': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'Img',
                }
            )
        }
      