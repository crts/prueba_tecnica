import re

from rest_framework import serializers

from .models import Gasto


class CustomValidationError(serializers.ValidationError):
    """Representa una excepción de validación personalizada.
        Args:
            serializers.ValidationError: La excepción de validación de Django REST Framework.
        Attributes:
            detail (dict): Un diccionario que contiene el campo y el mensaje de error.
        """
    def __init__(self, field, message):
        self.detail = {field: [message]}

class GastoSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Gasto."""
    class Meta:
        model = Gasto
        fields = '__all__'

    def validate_usuario(self, value):
        """Valida el nombre de usuario.
            Args:
                value (str): El valor del nombre de usuario a validar.
            Raises:
                ValidationError: Si el nombre de usuario contiene espacios en blanco o caracteres no válidos.
            Returns:
                None
            """
        if ' ' in value:
            raise CustomValidationError('usuario', "El nombre de usuario no puede contener "
                                                   "                espacios en blanco.")
        if not re.match(r'^[a-z0-9_.]+$', value):
            raise CustomValidationError('usuario',"El nombre de usuario solo puede contener "
                                                  "letras minúsculas, números y los caracteres especiales '_', '.'.")
        return value
    def validate_monto(self, value):
        """Valida el campo monto.
                Args:
                    value (Decimal): El valor del campo monto a validar.
                Raises:
                    CustomValidationError: Si el monto es menor o igual a cero.
                Returns:
                    Decimal: El valor del campo monto validado.
                """
        if value <= 0:
            raise CustomValidationError('monto', 'El monto debe ser mayor que cero.')
        return value

