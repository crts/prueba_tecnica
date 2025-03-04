from django.db import models

class Gasto(models.Model):
    """Representa el modelo de un gasto.
        Attributes:
            usuario (str): El nombre de usuario asociado al gasto.
            categoria (str): La categoría del gasto.
            monto (Decimal): El monto del gasto.
            fecha (Date): La fecha en la que se realizó el gasto.
        """
    usuario = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now=True)
