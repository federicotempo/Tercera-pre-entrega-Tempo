from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Sexo, Provincia
from .forms import ClienteForm

# Create your views here.


def crear_cliente(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home:home")
    else:
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})

# Código adicional para agregar informacion a la base de datos


sexo_1 = Sexo(nombre="Masculino")
sexo_2 = Sexo(nombre="Femenino")
sexo_1.save()
sexo_2.save()

provincia_1 = Provincia(nombre="Buenos Aires")
provincia_2 = Provincia(nombre="Catamarca")
provincia_3 = Provincia(nombre="Chaco")
provincia_4 = Provincia(nombre="Chubut")
provincia_5 = Provincia(nombre="Córdoba")
provincia_6 = Provincia(nombre="Corrientes")
provincia_7 = Provincia(nombre="Entre Ríos")
provincia_8 = Provincia(nombre="Formosa")
provincia_9 = Provincia(nombre="Jujuy")
provincia_10 = Provincia(nombre="La Pampa")
provincia_11 = Provincia(nombre="La Rioja")
provincia_12 = Provincia(nombre="Mendoza")
provincia_13 = Provincia(nombre="Misiones")
provincia_14 = Provincia(nombre="Neuquén")
provincia_15 = Provincia(nombre="Río Negro")
provincia_16 = Provincia(nombre="Salta")
provincia_17 = Provincia(nombre="San Juan")
provincia_18 = Provincia(nombre="San Luis")
provincia_19 = Provincia(nombre="Santa Cruz")
provincia_20 = Provincia(nombre="Santa Fe")
provincia_21 = Provincia(nombre="Santiago del Estero")
provincia_22 = Provincia(nombre="Tierra del Fuego")
provincia_23 = Provincia(nombre="Tucumán")

provincia_1.save()
provincia_2.save()
provincia_3.save()
provincia_4.save()
provincia_5.save()
provincia_6.save()
provincia_7.save()
provincia_8.save()
provincia_9.save()
provincia_10.save()
provincia_11.save()
provincia_12.save()
provincia_13.save()
provincia_14.save()
provincia_15.save()
provincia_16.save()
provincia_17.save()
provincia_18.save()
provincia_19.save()
provincia_20.save()
provincia_21.save()
provincia_22.save()
provincia_23.save()
