import re

from django.db import models
from rest_framework.exceptions import ValidationError


# Create your models here.
def validar_usuario(value):
    if ' ' in value:
        raise ValidationError("El nombre de usuario no puede contener espacios en blanco.")
    if not re.match(r'^[a-z0-9_.]+$', value):
        raise ValidationError("El nombre de usuario solo puede contener letras minúsculas, números y los caracteres especiales '_', '.'.")

class Gasto(models.Model):
    usuario = models.CharField(max_length=100, validators=[validar_usuario])
    categoria = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now=True)
