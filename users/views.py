from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserCreateForm, UserCompanyCreateForm
from .models import User
from django.urls import reverse

def home_view(request):
    return render(request, 'home.html')

def is_admin(user):
    """
    Verifica se o usuario e um administrador.
    """
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def user_list_view(request):
    """
    View para listar todos os usuários.
    Apenas administradores podem acessar.
    """
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def user_detail_view(request, id):
    """
    View para detalhar um usuário específico.
    Apenas administradores podem acessar.
    """
    user = get_object_or_404(User, id=id)
    return render(request, 'users/user_detail.html', {'user_detail': user})

@login_required
@user_passes_test(is_admin)
def user_delete_view(request, id):
    """
    View para deletar um usuário existente.
    Apenas administradores podem acessar.
    """
    user_obj = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user_obj.delete()
        messages.success(request, "Usuário deletado com sucesso.")
        return redirect('user:listar_user')
    return render(request, 'users/user_confirm_delete.html', {'user_obj': user_obj})

def register_view(request):
    """
    View para registrar um usuário comum ou uma empresa.
    """
    user_type = request.GET.get('type')
    
    if request.method == 'POST':
        if user_type == 'company':
            form = UserCompanyCreateForm(request.POST)
        else:
            form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Registro realizado com sucesso.")
            
            # Redirecionar com base no tipo de usuário
            if user_type == 'company':
                return redirect('user:empresa_dashboard')  # Redireciona para o dashboard da empresa
            else:
                return redirect('user:usuario_dashboard')  # Redireciona para o dashboard do usuário comum
    else:
        if user_type == 'company':
            form = UserCompanyCreateForm()
        else:
            form = UserCreateForm()

    template_name = 'users/criar_empresa.html' if user_type == 'company' else 'users/criar_user.html'
    return render(request, template_name, {'form': form, 'title': 'Registrar como Empresa' if user_type == 'company' else 'Registrar como Usuário Comum'})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    def get_redirect_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_company:
                return reverse('user:empresa_dashboard')
            else:
                return reverse('user:usuario_dashboard')
        return super().get_redirect_url()

@login_required
def usuario_dashboard_view(request):
    if request.user.is_authenticated:
        saudacao = f"Olá, {request.user.nome}!"
    else:
        saudacao = "Olá, visitante!"
    """
    Dashboard para o usuário comum.
    Apenas usuários autenticados podem acessar.
    """
    context = {
        'user': request.user,
        'saudacao': saudacao # Passa o usuário autenticado para o template
    }
    return render(request, 'users/dashboard_user.html', context)

@login_required
def empresa_dashboard_view(request):
    """
    Dashboard para empresas.
    Apenas usuários autenticados podem acessar.
    """
    if request.user.is_authenticated:
        saudacao = f"Olá, {request.user.nome_empresa}!"

    context = {
        'user': request.user,
        'saudacao': saudacao  # Passa o usuário autenticado para o template
    }
    return render(request, 'users/dashboard_empresa.html', context)
