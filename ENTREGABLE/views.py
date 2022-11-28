from django.shortcuts import render
from .models import Integrante
from django.http import HttpResponse
from django.template import Template,Context,loader

# Create your views here.

def persona(request):
    persona1=Integrante(nombre="Leandro", apellido="Di Palma", edad="41", ocupacion="Administrativo", diadenacimiento=("1981-02-07"))
    persona1.save()
    persona2=Integrante(nombre="Eliana", apellido="Alarcon", edad="38", ocupacion="Estilista", diadenacimiento=("1984-04-12"))
    persona2.save()
    persona3=Integrante(nombre="Santino", apellido="Di Palma", edad="16", ocupacion="Estudiante", diadenacimiento=("2006-03-06"))
    persona3.save()
    cadena_detexto=persona.nombre+" "+persona.apellido+" "+str(persona.edad)+" "+persona.ocupacion+" "+str(persona.diadenacimmiento)
    return HttpResponse(cadena_detexto)

def template (request):
    nombre="Leandro"
    apellido="Di Palma"
    diccionario={"nombre":nombre, "apellido":apellido}
    
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)


