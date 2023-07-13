from django.shortcuts import render

def home(request):
    contexto = {"saludo": "hola"}
    return render(request, "Home/index.html", contexto)
