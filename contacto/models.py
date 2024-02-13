from django.db import models

# Create your models here.
class Contacto(models.Model):
    def __str__(self) -> str:
        return f' Nombre: {self.nombre} {self.apellido} Telefono:{self.telefono} Mail:{self.mail}'
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    telefono=models.IntegerField()
    mail=models.EmailField()