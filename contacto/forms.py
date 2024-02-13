from django import forms

class Formulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    telefono=forms.IntegerField()
    mail=forms.EmailField()