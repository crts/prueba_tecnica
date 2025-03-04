from rest_framework_simplejwt.views import TokenObtainPairView

from token_api.serializers import TokenObtainSerializer


class TokenObtainView(TokenObtainPairView):
    """Vista personalizada para obtener un token JWT.

      Esta vista se utiliza para obtener un token JWT utilizando el serializador personalizado `TokenObtainSerializer`.
      """
    serializer_class = TokenObtainSerializer