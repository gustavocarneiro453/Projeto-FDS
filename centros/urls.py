from django.urls import path
from .views import cadastrar_centro, lista_centros, update_centros, remover_centros

app_name = 'centros'

urlpatterns = [
    path('cadastrar/', cadastrar_centro, name='cadastrar_centro'),
    path('lista/', lista_centros, name='lista_centros'),  # URL para listar os centros
    path('atualizar/<int:centro_id>/', update_centros, name='update_centros'),
    path('remover/<int:centro_id>/', remover_centros, name='remover_centro')
]
