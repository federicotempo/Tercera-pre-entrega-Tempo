from django.contrib import admin

from .models import Ciudad, Cliente, Sexo

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Ciudad)
admin.site.register(Sexo)
