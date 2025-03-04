from rest_framework_simplejwt.views import TokenObtainPairView

from token_api.serializers import TokenObtainSerializer


class TokenObtainView(TokenObtainPairView):
    serializer_class = TokenObtainSerializer