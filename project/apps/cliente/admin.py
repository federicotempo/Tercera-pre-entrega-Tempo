from django.contrib import admin

from .models import Cliente, Provincia, Sexo

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Provincia)
admin.site.register(Sexo)
