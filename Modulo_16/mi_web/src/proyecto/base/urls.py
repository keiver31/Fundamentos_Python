#Integro el urls.py de proyecto
from django.urls import path
#from . import views
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView


#urlpatterns = [path('', views.lista_pendientes, name='pendientes')]#Invoco la función de base\views.py

urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('login/', Logueo.as_view(), name='login'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')]#Invoco la función de base\views.py