from rest_framework import serializers

from .models import Gasto


class CustomValidationError(serializers.ValidationError):
    def __init__(self, field, message):
        self.detail = {field: [message]}

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'

    def validate_monto(self, value):
        if value <= 0:
            raise CustomValidationError('monto', 'El monto debe ser mayor que cero.')
        return value

