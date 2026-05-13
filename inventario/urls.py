from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('productos/', views.productos, name='productos'),

    path(
        'crear-producto/',
        views.crear_producto,
        name='crear_producto'
    ),

    path(
        'editar-producto/<int:id>/',
        views.editar_producto,
        name='editar_producto'
    ),

    path(
        'eliminar-producto/<int:id>/',
        views.eliminar_producto,
        name='eliminar_producto'
    ),
    
    path(
        'crear-producto/',
        views.crear_producto,
        name='crear_producto'
    ),
    path('ventas/', views.ventas, name='ventas'),
]