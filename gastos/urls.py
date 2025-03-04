from django.urls import path
from gastos import views as vs

urlpatterns = [
    path(r'gastos/', vs.GastoList.as_view(), name='gasto-list'),
    path(r'gastos/<int:pk>/', vs.GastoDetail.as_view(), name='gasto-detail'),

]