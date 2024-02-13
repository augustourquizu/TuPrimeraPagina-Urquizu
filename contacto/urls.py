from django.urls import path
from contacto.views import crear_contacto, contactos
urlpatterns= [
    path("crear_contacto/", crear_contacto, name="formulario"),
    path("contactos", contactos, name="contactos" )
    ]