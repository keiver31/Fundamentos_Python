from django.db import models
from django.contrib.auth.models import User #Importa modelo de djando

# Create your models here.

class Tarea(models.Model): #Se especifica models.Model, de modo que especifica que es un modelo
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,
                                null=True,
                                blank=True) #Si se elimina el usuario, se elimina todo lo que creo
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                  blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering =['completo'] #Se debe migrar la base de datos creada
