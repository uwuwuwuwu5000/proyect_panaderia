//Validacion formulario suscripcion -Commit final
$().ready(function(){
    $("#bol").validate({
        rules:{
            noms:{
                required:true,
                nowhitespace:true,
                lettersonly:true
            },
            apes:{
                required:true,
                nowhitespace:true,
                lettersonly:true
            },
            mail:{
                required:true,
                email:true
            },
            fono:{
                required:true,
                minlength:9
            },
            genero:"required"
        },
        messages:{
            noms: {
                required: "Por favor ingrese sus nombres.",
                nowhitespace: "No deje espacios vacíos",
                lettersonly: "Por favor ingrese solo letras."
            },
            apes: {
                required: "Por favor ingrese sus apellidos.",
                nowhitespace: "No deje espacios vacíos",
                lettersonly: "Por favor ingrese solo letras."
            },
            mail:{
                required:"Por favor ingrese su correo electrónico.",
                email:"Por favor ingrese un correo válido."
            },
            fono:{
                required:"Por favor ingrese un número de celular.",
                minlength:"Por favor ingrese un número de mínimo 9 carácteres."
            },
            genero:"Por favor seleccione una de las opciones de género."
        }
    });
});

//Validacion formulario cursos
$(document).ready(function(){
    $("#cursoForm").validate({
        rules:{
            nombre:{
                required:true,
                nowhitespace:true,
                lettersonly:true
            },
            apellido:{
                required:true,
                nowhitespace:true,
                lettersonly:true
            },
            email:{
                required:true,
                email:true
            },
            direccion:{
                required:true,
                minlength:4,

            },
            edad:{
                required:true,
                min:16,
                max: 99,
                number: true
            },
            sexo:"required",
            curso:"required",
            horario:"required"

        },
        messages:{
            nombre: {
                required: "Por favor ingrese su nombre",
                nowhitespace: "Caracter invalido",
                lettersonly: "Caracter invalido"
            },
            apellido: {
                required: "Por favor ingrese su apellido",
                nowhitespace: "Caracter invalido",
                lettersonly: "Caracter invalido"
            },
            email:{
                required:"Por favor ingrese un email.",
                email:"Ingrese un email valido."
            },
            direccion:{
                required:"Por favor ingrese una direccion.",
                minlength:"La direccion al menos debe tener 4 caracteres."
            },
            edad:{
                required:"Por favor ingrese una edad.",
                min:"El mínimo aceptado es 16.",
                max:"Por favor ingrese una edad valida.",
                number:"Por favor ingrese una edad valida."
            },
            sexo:"Seleccione una opcion",
            curso:"Seleccione un curso",
            horario:"Seleccione un horario"
        }
    })
});

//Validación editar producto
$(document).ready(function(){
    $("#formProd").validate({
        rules: {
            "nomProducto": {
                required: true,
                lettersonly: true,
                minlength: 2
            },
            "descProducto": {
                required: true,
                minlength: 20
            },
            "imagen":{
                required: true,
                accept: "image/*"
            },
            "precio": {
                required: true,
                min: 1
            }
        },
        messages: {
            "nomProducto": {
                required: "Debe ingresar un nombre para el producto.",
                lettersonly: "Solo ingrese letras.",
                minlength: "El largo debe ser mayor a 2 caracteres."
            },
            "descProducto": {
                required: "Debe ingresar una descripción para el producto",
                minlength: "La descripción debe ser de mínimo 20 carácteres."
            },
            "imagen":{
                required: "Debe rellenar este campo.",
                accept: "Solo puede subir imágenes."
            },
            "precio": {
                required: "Debe ingresar un precio",
                min: "El precio debe ser mayor a 0"
            }
        }
    });
});

//Validación crear producto
$(document).ready(function(){
    $("#formProdC").validate({
        rules: {
            "idProducto": {
                required: true,
                nowhitespace: true
            },
            "nomProducto": {
                required: true,
                lettersonly: true,
                minlength: 2
            },
            "descProducto": {
                required: true,
                minlength: 20,
            },
            "imagen":{
                required: true,
                accept: "image/*"
            },
            "precio":{
                required: true,
                min: 1
            }
        },
        messages: {
            "idProducto": {
                required: "Debe rellenar este campo.",
                nowhitespace: "No se permiten espacios blancos."
            },
            "nomProducto": {
                required: "Debe rellenar este campo.",
                lettersonly: "Solo caracteres alfabéticos.",
                minlength: "Utilice mínimo 2 carácteres."
            },
            "descProducto": {
                required: "Debe rellenar este campo.",
                minlength: "Utilice mínimo 20 carácteres.",
            },
            "imagen":{
                required: "Debe rellenar este campo.",
                accept: "Solo puede subir imágenes."
            },
            "precio":{
                required: "Debe rellenar este campo.",
                min: "El precio debe ser mayor a 0"
            }
        }
    });
});

//validación formulario registro usuario
$(document).ready(function(){
    $("#usuario").validate({
        rules: {
            "username": {
                required: true,
                nowhitespace: true,
                minlength: 5
            },
            "first_name": {
                required: true,
                nowhitespace: true,
                lettersonly: true,
                minlength: 2
            },
            "last_name": {
                required: true,
                nowhitespace: true,
                lettersonly: true,
                minlength: 2
            },
            "email": {
                required: true,
                email: true
            },
            "password1": {
                required: true,
                minlength: 8
            },
            "password2": {
                required: true,
                minlength: 8,
                equalTo: "#id_password1"
            }
        },
        messages: {
            "username": {
                required: "Debe rellenar este campo.",
                nowhitespace: "No deje espacios vacíos.",
                minlength: "Ocupe un mínimo de 5 carácteres."
            },
            "first_name": {
                required: "Debe rellenar este campo.",
                nowhitespace: "No deje espacios vacíos.",
                lettersonly: "Solo ingrese letras",
                minlength: "Ocupe un mínimo de 2 carácteres."
            },
            "last_name": {
                required: "Deber rellenar este campo.",
                nowhitespace: "No deje espacios vacíos.",
                lettersonly: "Solo ingrese letras",
                minlength: "Ocupe un mínimo de 2 carácteres."
            },
            "email": {
                required: "Debe rellenar este campo.",
                email: "Ingrese un correo válido."
            },
            "password1": {
                required: "Debe rellenar este campo.",
                minlength: "Ocupe un mínimo de 8 carácteres."
            },
            "password2": {
                required: "Debe rellenar este campo.",
                minlength: "Ocupe un mínimo de 8 carácteres.",
                equalTo: "Las contraseñas no coinciden"
            }
        },
        errorPlacement: function(error, element) {
            error.addClass("invalid-feedback");
            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.next("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function(element, errorClass, validClass) {
            $(element).addClass("is-invalid").removeClass("is-valid");
        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).addClass("is-valid").removeClass("is-invalid");
        }
    });
});

//Validación Modificación Perfil
$(document).ready(function(){
    $("#modPerfil").validate({
        rules: {
            "first_name": {
                required: true,
                nowhitespace: true,
                lettersonly: true,
                minlength: 2
            },
            "last_name": {
                required: true,
                nowhitespace: true,
                lettersonly: true,
                minlength: 2
            },
            "email": {
                required: true,
                email: true
            },
            "password1": {

                minlength: 8
            },
            "password2": {
                minlength: 8,
                equalTo: "#id_password1"
            }
        },
        messages: {
            "first_name": {
                required: "Debe rellenar este campo.",
                nowhitespace: "No deje espacios vacíos.",
                lettersonly: "Solo ingrese letras",
                minlength: "Ocupe un mínimo de 2 carácteres."
            },
            "last_name": {
                required: "Deber rellenar este campo.",
                nowhitespace: "No deje espacios vacíos.",
                lettersonly: "Solo ingrese letras",
                minlength: "Ocupe un mínimo de 2 carácteres."
            },
            "email": {
                required: "Debe rellenar este campo.",
                email: "Ingrese un correo válido."
            },
            "password1": {
                minlength: "Ocupe un mínimo de 8 carácteres."
            },
            "password2": {
                minlength: "Ocupe un mínimo de 8 carácteres.",
                equalTo: "Las contraseñas no coinciden"
            }
        },
        errorPlacement: function(error, element) {
            error.addClass("invalid-feedback");
            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.next("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function(element, errorClass, validClass) {
            $(element).addClass("is-invalid").removeClass("is-valid");
        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).addClass("is-valid").removeClass("is-invalid");
        }
    });
});


//Validacion crear curso
$(document).ready(function(){
    $("#formCurso").validate({
        rules: {
            "idCurso": {
                required: true
            },
            "nomCurso": {
                required: true,
                minlength:2,
                maxlength:50
            },
            "descCurso": {
                required: true,
                minlength: 10,
                maxlength:300
            },
            "precioCurso": {
                required: true,
                min: 1,
                max: 999999
            },
            "duracion": {
                required: true,
                minlength: 2,
                maxlength:15
            },
            "cupos": {
                required: true,
                min: 5,
            },
            "horario": {
                required: true,
            },
            "fechaInicio": {
                required: true,
            },
            "img":{
                required: true,
                accept: "image/*"
            }
            
        },
        messages: {
           "idCurso": {
                required: "Debe rellenar este campo"
            },
            "nomCurso": {
                required: "Debe rellenar este campo",
                minlength: "Debe ingresar un nombre mas largo.",
                maxlength:"Nombre del curso demasiado largo"
            },
            "descCurso": {
                required: "Debe rellenar este campo",
                minlength: "Debe ingresar una descripcion de mas de 10 caracteres.",
                maxlength: "Descripcion demasiado larga"
            },
            "precioCurso": {
                required: "Debe rellenar este campo",
                min: "Precio invalido",
                max:"Precio invalido"
            },
            "duracion": {
                required: "Debe rellenar este campo",
                minlength: "El minimo de caracteres es 2",
                maxlength: "Maximo de caracteres es 15"
            },
            "cupos": {
                required: "Debe rellenar este campo",
                min: "El minimo de cupos es 5",
            },
            "horario": {
                required: "Debe rellenar este campo",
            },
            "fechaInicio": {
                required: "Debe rellenar este campo",
            },
            "img":{
                required: "Debe rellenar este campo.",
                accept: "Solo se pueden subir imagenes"
            }
        }
    });
});
//Validacion del modificar curso
$(document).ready(function(){
    $("#formCursoM").validate({
        rules: {
            "idCurso": {
                required: true,
            },
            "nomCurso": {
                required: true,
                minlength:2,
                maxlength:50
            },
            "descCurso": {
                required: true,
                minlength: 10,
                maxlength:300
            },
            "precioCurso": {
                required: true,
                min: 1,
                max: 999999
            },
            "duracion": {
                required: true,
                minlength: 2,
                maxlength:15
            },
            "cupos": {
                required: true,
                min: 5,
            },
            "horario": {
                required: true,
            },
            "fechaInicio": {
                required: true,
            },
            "fechaTermino": {
            },
            "img":{
                accept: "image/*"
            }
            
        },
        messages: {
           "idCurso": {
                required: "Debe rellenar este campo",
            },
            "nomCurso": {
                required: "Debe rellenar este campo",
                minlength: "Debe ingresar un nombre mas largo.",
                maxlength:"Nombre del curso demasiado largo"
            },
            "descCurso": {
                required: "Debe rellenar este campo",
                minlength: "Debe ingresar una descripcion de mas de 10 caracteres.",
                maxlength: "Descripcion demasiado larga"
            },
            "precioCurso": {
                required: "Debe rellenar este campo",
                min: "Precio invalido",
                max:"Precio invalido"
            },
            "duracion": {
                required: "Debe rellenar este campo",
                minlength: "El minimo de caracteres es 2",
                maxlength: "Maximo de caracteres es 15"
            },
            "cupos": {
                required: "Debe rellenar este campo",
                min: "El minimo de cupos es 5",
            },
            "horario": {
                required: "Debe rellenar este campo",
            },
            "fechaInicio": {
                required: "Debe rellenar este campo",
            },
            "img":{
                accept: "Solo se pueden subir imagenes"
            }
        }
    });
});




//Cursos.json

// const url = 'http://localhost:3000/cursos';
// fetch(url)
// .then (response => response.json())
// .then (data => mostrarData(data))
// .then (error => console.log(error))

// const mostrarData = (data) => {
//     console.log(data)
//     let body = ""
//     for (var i = 0 ; i < data.length; i++) {
//         body += `<div class="row mx-2 py-3">
//         <img src="${data[i].img}" class="col-lg-3 img-fluid curso-img px-0"  alt="curso">
//         <div class="col texto-curso">
//         <h3 class="text-start"><b>Curso: ${data[i].nombre}</b></h3>
//                     <p>${data[i].descripcion}</p>
//                     <p><b>Precio: </b>${data[i].precio}</p>
//                     <p><b>Duracion: </b>${data[i].duracion}</p>
//                     <p><b>Cupos: </b>${data[i].cupos}</p>
//                     <p><b>Horario: </b>${data[i].horario}</p>
//                     <p><b>Fechas: </b> ${data[i].fecha}</p>
//                     </div>
//         </div>
//         `
//     }
//     document.querySelector('#cursos-body').innerHTML=body;
// }

//Api pública de comentarios
function mostrarComentarios(){
    let url2='https://jsonplaceholder.typicode.com/comments'
    fetch(url2)
    .then(response => response.json())
    .then(data => mostrarData(data))
    .catch(error => console.log(error))

    const mostrarData=(data)=>{
        console.log(data)
        let body=""
        for(var i=0; i<10;i++){
            body+=`<tr>
            <td>${data[i].id}</td>
            <td>${data[i].name}</td>
            <td>${data[i].body}</td>
            </tr>`
        }
        document.getElementById('comentarios').innerHTML=body
    }
}


//Reloj

function reloj(){
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();

    if (hh<10) {
        hh = "0"+hh;
    }
    if (mm<10) {
        mm = "0"+mm;
    }
    if (ss<10) {
        ss = "0"+ss;
    }

    let time = hh + ":" + mm + ":" + ss 

    let watch = document.querySelectorAll('.reloj');
    watch[0].innerHTML = time;
    watch[1].innerHTML = time;
};

setInterval(reloj, 1000);


