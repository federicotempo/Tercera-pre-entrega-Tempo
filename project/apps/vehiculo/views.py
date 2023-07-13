from django.shortcuts import render
# Create your views here.

def home(request):
    contexto = {"app": "Aplicación Vehiculos"}
    return render(request, "vehiculo/index.html", contexto)
