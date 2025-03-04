from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenObtainSerializer(TokenObtainPairSerializer):
    """Serializador personalizado para obtener un token JWT.

    Este serializador se utiliza para obtener un token JWT y se agrega el nombre de usuario al token.
    """
    @classmethod
    def get_token(cls, user):
        """Obtiene un token JWT para el usuario.

               Args:
                   user (User): El objeto de usuario para el cual se generará el token.

               Returns:
                   Token: El token JWT para el usuario.
               """
        token = super().get_token(user)
        token['username'] = user.username
        return token