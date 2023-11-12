from django.contrib import admin
from .models import Tarea #Importada

# Register your models here.
admin.site.register(Tarea) #Tabla que se requiere registrar, permite la visualización en el server
