from django.urls import path
from AppMotos.views import *
app_name = "AppMotos"


urlpatterns = [
    path("Motos", MotosDB, name = "Motos-Inicio"),
    path("motos/crear/", MotoFormulario, name = "motos-formulario"),



]