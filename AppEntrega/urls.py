
from django.urls import path
from AppEntrega.views import cliente,producto,tienda,registro,busquedaCliente,busquedaProducto,busquedaTienda

urlpatterns = [
    
    path('cliente',cliente,name="AppEntregaCliente"),
    path('producto',producto,name="AppEntregaProducto"),
    path('tienda',tienda,name="AppEntregaTienda"),
    path('registro',registro,name="AppEntregaRegistro"),
    path('busquedaCliente',busquedaCliente,name="AppEntregaBusquedaC"),
    path('busquedaProducto',busquedaProducto,name="AppEntregaBusquedaP"),
    path('busquedaTienda',busquedaTienda,name="AppEntregaBusquedaT"),
    
    
]