from django.db import models
from django import forms
# Create your models here.

class usuario(models.Model):
    nombres=models.CharField(max_length=30,null=False,blank=False)
    apellidos=models.CharField(max_length=30,null=False,blank=False)
    dni=models.CharField(max_length=8,unique=True,null=False,blank=False)
    FechaNacimiento=models.DateField('Fecha de Nacimiento',null=False,blank=False)
    SEXOS=(('F','Femenino'),('M','Masculino'))
    Sexo=models.CharField(max_length=1,choices=SEXOS,default='M' )
    usuario=models.CharField('Nombre de usuario',max_length=20,unique=True,null=False,blank=False)
    clave=models.CharField('Contraseña',max_length=20,null=False,blank=False)

    def usuariocompleto(self):

        cadena="{1}, {0}"
        return cadena.format(self.apellidos,self.nombres)

    def __str__(self):
        return self.usuariocompleto()
