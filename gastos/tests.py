import pytest
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework_simplejwt.tokens import AccessToken
from gastos.views import GastoList, GastoDetail
from gastos.models import Gasto
from django.contrib.auth.models import User


@pytest.fixture
def api_request_factory():
    return APIRequestFactory()


@pytest.fixture
def authenticated_request(api_request_factory, django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='testpassword')
    access_token = AccessToken()
    request = api_request_factory.get('/gastos/')
    force_authenticate(request, user=user, token=access_token)
    return request


@pytest.mark.django_db
def test_gasto_list_get(authenticated_request):
    # Crea algunos objetos Gasto para la prueba
    Gasto.objects.create(usuario='user1', categoria='cat1', monto=10.0)
    Gasto.objects.create(usuario='user2', categoria='cat2', monto=20.0)

    # Realiza una solicitud GET a la vista GastoList
    view = GastoList.as_view()
    response = view(authenticated_request)
    # Verifica que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200




@pytest.mark.django_db
def test_gasto_detail_get(authenticated_request):
    # Crea un objeto Gasto para la prueba
    gasto = Gasto.objects.create(usuario='user4', categoria='cat4', monto=40.0)

    # Realiza una solicitud GET a la vista GastoDetail
    view = GastoDetail.as_view()
    response = view(authenticated_request, pk=gasto.pk)

    # Verifica que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200

