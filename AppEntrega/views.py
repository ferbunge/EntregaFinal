import http
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppEntrega.models import empleados, clientes, proveedores
from AppEntrega.forms import Formulario

# Create your views here.

def principal(request):

      return render(request, "AppEntrega/inicio.html")

def inicio(request):

      return render(request, "AppEntrega/inicio.html")

def proveedor(request):

      return render(request, "AppEntrega/proveedor.html")      

def empleado(request):
    
       return render(request, "AppEntrega/empleado.html")

def cliente(request):

       return render(request, "AppEntrega/cliente.html")

def busquedaClientes(request):

    return render (request, "AppEntrega/busquedaClientes.html")

def buscar(request):
    
    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        resultado = clientes.objects.filter(nom=nombre)

        return render(request, "AppEntrega/resultadosBusqueda.html", {"resultado":resultado})
    else:

        return render(request, "AppEntrega/busquedaClientes.html", {"Error":"No se ingresó ningún nombre"})
   
def clienteFormulario(request): ## ESTO ES PARA DJANGO
    if (request.method=="POST"): ##Ahora no va a traer datos, sino va a traer un formulario.
        form=Formulario(request.POST) ##Creo una variable, para recibir el formulario.
        print(form) #lo imprime
        if form.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= form.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            nombre=info["nombre"]
            id=info["id"]
            email=info["email"]
            Cliente= clientes(nom=nombre, id=id, mail=email)
            Cliente.save() ##lo guardas en caso de que sea valido.
            return render (request, "AppEntrega/inicio.html")
    else: #Si no viene por POST
        form=Formulario() #Creo el formulario vacio
    return render(request, "AppEntrega/clienteFormulario.html", {"form":form})##lo renderizo y se lo mando como un diccionario para que lo pueda usar mi pantalla, mi template, como una variable.
    ##formulario de arriba tiene que ser el mismo que aparece en el html para usar
def empleadoFormulario(request): ## ESTO ES PARA DJANGO
    if (request.method=="POST"): ##Ahora no va a traer datos, sino va a traer un formulario.
        form=Formulario(request.POST) ##Creo una variable, para recibir el formulario.
        print(form) #lo imprime
        if form.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= form.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            nombre=info["nombre"]
            id=info["id"]
            email=info["email"]
            Empleado= empleados(nom=nombre, id=id, mail=email)
            Empleado.save() ##lo guardas en caso de que sea valido.
            return render (request, "AppEntrega/inicio.html")
    else: #Si no viene por POST
        form=Formulario() #Creo el formulario vacio
    return render(request, "AppEntrega/empleadoFormulario.html", {"form":form})

def proveedorFormulario(request): ## ESTO ES PARA DJANGO
    if (request.method=="POST"): ##Ahora no va a traer datos, sino va a traer un formulario.
        form=Formulario(request.POST) ##Creo una variable, para recibir el formulario.
        print(form) #lo imprime
        if form.is_valid(): ##identificar que lo que llega como formulario es validad (int, str, etc)
            info= form.cleaned_data #Limpiame los datos y damelo en la variable info. Es un diccionario con la info.
            print(info) ##para que veamos la diferencia del cleaned
            nombre=info["nombre"]
            id=info["id"]
            email=info["email"]
            Proveedor= proveedores(nom=nombre, id=id, mail=email)
            Proveedor.save() ##lo guardas en caso de que sea valido.
            return render (request, "AppEntrega/inicio.html")
    else: #Si no viene por POST
        form=Formulario() #Creo el formulario vacio
    return render(request, "AppEntrega/proveedorFormulario.html", {"form":form})