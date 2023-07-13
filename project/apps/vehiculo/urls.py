from django.urls import path
from .views import home

app_name = "vehiculo"

urlpatterns = [
    path('', home, name="home"),
]
