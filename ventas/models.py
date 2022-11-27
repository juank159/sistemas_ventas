from django.db import models
from datetime import datetime

# Create your models here.

class Tipo(models.Model):
    nombre=models.CharField(max_length=70, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

class Empleado(models.Model):
    tipo=models.ForeignKey(Tipo, verbose_name='Tipo', on_delete=models.CASCADE)
    nombre=models.CharField(max_length=150, verbose_name='Nombre')
    documento=models.CharField(max_length=20, unique= True, verbose_name='Documento')
    fecha_registro=models.DateField(default=datetime.now(),verbose_name='Fecha de Registro')
    fecha_creacion=models.DateTimeField(auto_now=True)
    Fecha_actualizacion=models.DateTimeField(auto_now_add=True)
    celular=models.PositiveIntegerField(default=0)
    salario=models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    estado=models.BooleanField(default=True)
    fotografia=models.ImageField(upload_to= 'avatar/%y/%m/%d', null=True, blank=True)
    documentos=models.FileField(upload_to= 'cvitae/%y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.nombre


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']