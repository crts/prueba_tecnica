from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from token_api import views as vs

urlpatterns = [

    path('token/', vs.TokenObtainView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]