from django.db import models

class pqrs(models.Model):
    numero_documento = models.CharField(max_length=70, blank=False, default='')
    nombres_apellidos = models.CharField(max_length=200,blank=False, default='')
    telefono_fijo = models.CharField(max_length=200,blank=False, default='')
    celular = models.CharField(max_length=200,blank=False, default='')
    email = models.CharField(max_length=200,blank=False, default='')
    titulo_pqr = models.CharField(max_length=200,blank=False, default='')
    descripcion_pqr = models.CharField(max_length=200,blank=False, default='')
    estado_pqr = models.CharField(max_length=200,blank=False, default='')
    fecha = models.CharField(max_length=200,blank=False, default='')
    
    

