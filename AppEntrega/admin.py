from http import client
from django.contrib import admin
# Register your models here.
from .models import *


admin.site.register(empleados)

admin.site.register(clientes)

admin.site.register(proveedores)
