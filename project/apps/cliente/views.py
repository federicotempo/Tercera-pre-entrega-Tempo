from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    return render(request, "cliente/index.html", contexto)

def crear_cliente(request: HttpRequest) -> HttpResponse:
    
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:
        form = ClienteForm()
    return render(request, "cliente/crear.html", {"form": form})