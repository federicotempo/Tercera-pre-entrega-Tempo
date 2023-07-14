from django.urls import path
from .views import crear_cliente

app_name = "cliente"

urlpatterns = [

    path('crear_cliente', crear_cliente, name="crear_cliente"),
]
