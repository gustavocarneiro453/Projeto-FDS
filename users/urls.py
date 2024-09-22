from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import (
    user_detail_view,
    user_list_view,
    #user_update_view,
    user_delete_view,
    #user_register_view,
    #company_register_view,
    register_view,

)

app_name = 'user'

urlpatterns = [
    path('', user_list_view, name='listar_user'), 
    #path('criar-centro/', criar_centro, name='criar-centro'),  # Nova rota para criar centro, se aplicável
    path('<int:id>/', user_detail_view, name='user-detail'), 
    #path('<int:id>/update/', user_update_view, name='user-update'),  # Rota para atualizar usuário
    path('<int:id>/delete/', user_delete_view, name='user-delete'),  # Rota para deletar usuário
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('registrar/', register_view, name='register'),
    #path('registrar/empresa/', company_register_view, name='register_company'),

]
