from threading import main_thread
from django.urls import path
from .views import *


urlpatterns = [
    path('inicio', inicio),
    path('cliente/', cliente, name="Clientes"),
    path('proveedores/', proveedor, name="Proveedor"),
    path('empleado/', empleado, name="Empleado"),
    path('busquedaClientes/', busquedaClientes, name="busquedaClientes"),
    path('buscar/', buscar, name="buscar"),
    path('clienteFormulario/', clienteFormulario, name="clienteFormulario"),
    path('empleadoFormulario/', empleadoFormulario, name="empleadoFormulario"),
    path('proveedorFormulario/', proveedorFormulario, name="proveedorFormulario"),
    path('', principal, name="Principal")
]

