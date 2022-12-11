
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppMotos.models import MotosDB
from AppMotos.forms import MotoFormulario


def MotosFormuario(request):
    if request.method == 'POST':
        formulario = MotoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.clean_data()

            moto = MotosDB(marca=data["marca"], modelo = data["modelo"], kilometros = data["kilometros"], precio = data["precio"], foto= data["foto"])

            moto.save()
        
        else:
            errores = formulario.errors
    

    formulario = MotoFormulario()

    contexto = {"formulario": formulario}

    return render(request, "AppMotos/Motos_formulario.html", contexto)




# Create your views here.

