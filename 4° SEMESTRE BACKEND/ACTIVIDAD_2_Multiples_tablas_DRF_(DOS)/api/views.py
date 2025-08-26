from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Bienvenido a la actividad Múltiples Tablas</h1><p>API funcionando correctamente.</p>")
