from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('base/', views.base, name='base'),
    path('clientes/', views.clientes, name='clientes'),
    path('login/', views.iniciar_sesion, name='login'), 
  
    path('administrar/servicios/', views.administrar_servicios, name='administrar_servicios'),
    path('administrar/servicios/<int:id>/editar/', views.editar_servicio, name='editar_servicio'),
    path('administrar/servicios/<int:id>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),

 
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),

    path('clientes/registro/', views.clientes, name='clientes'),

    
    path('administrar/clientes/', views.ClienteListView.as_view() if hasattr(views, 'ClienteListView') else views.clientes, name='administrar_clientes'),
    path('administrar/clientes/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('administrar/clientes/<int:id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),

    path('barberos/', views.barberos, name='barberos'),
    path('contactos/', views.contactos, name='contactos'),
    path('reservas/', views.reservas, name='reservas'),
]

