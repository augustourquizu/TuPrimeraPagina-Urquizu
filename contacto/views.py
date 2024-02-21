from django.shortcuts import render, redirect
from django.http import HttpResponse
from contacto.forms import Formulario
from contacto.models import Contacto
# Create your views here.
def inicio(request):
    return render(request, "inicio.html", locals())

def contactos(request):
    contactos=Contacto.objects.all()
    return render(request, 'contactos.html', {"contactos":contactos})
    
def crear_contacto(request):
    formulario=Formulario()
    if request.method=='POST':
        formulario=Formulario(request.POST)
        if formulario.is_valid():
            nombre=formulario.cleaned_data.get("nombre")
            apellido=formulario.cleaned_data.get("apellido")
            telefono=formulario.cleaned_data.get("telefono")
            mail=formulario.cleaned_data.get("mail")
            contacto=Contacto(nombre=nombre, apellido=apellido, telefono=telefono, mail=mail)
            contacto.save()
            return redirect('inicio')
    return render(request, "formulario.html", {"formulario":formulario})
