from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UserCreateForm, UserCompanyCreateForm
from .models import User

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

# @login_required
# @user_passes_test(is_admin)
# def user_update_view(request, id):
#     """
#     View para atualizar um usuário existente.
#     Apenas administradores podem acessar.
#     """
#     user_obj = get_object_or_404(User, id=id)
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST, instance=user_obj)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Usuário atualizado com sucesso.")
#             return redirect('user:user-detail', id=user_obj.id)
#         else:
#             messages.error(request, "Por favor, corrija os erros abaixo.")
#     else:
#         form = UserUpdateForm(instance=user_obj)
#     return render(request, 'users/user_form.html', {'form': form, 'title': 'Atualizar Usuário'})

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

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# def user_register_view(request):
#     """
#     View para registrar um usuário comum.
#     """
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid() and not form.cleaned_data['is_company']:
#             form.save()
#             return redirect('login')  # Redireciona para a página de login após o registro
#     else:
#         form = UserCreateForm(initial={'is_company': False})  # Define como usuário comum
#     return render(request, 'users/criar_user.html', {'form': form, 'title': 'Registrar como Usuário Comum'})

# def company_register_view(request):
#     """
#     View para registrar uma empresa.
#     """
#     if request.method == 'POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid() and form.cleaned_data['is_company']:
#             form.save()
#             return redirect('login')  # Redireciona para a página de login após o registro
#     else:
#         form = UserCompanyCreateForm(initial={'is_company': True})  # Define como empresa
#     return render(request, 'users/criar_empresa.html', {'form': form, 'title': 'Registrar como Empresa'})

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
            form.save()
            messages.success(request, "Registro realizado com sucesso.")
            return redirect('login')  # Redirecionar após o registro
    else:
        if user_type == 'company':
            form = UserCompanyCreateForm()
        else:
            form = UserCreateForm()

    template_name = 'users/criar_empresa.html' if user_type == 'company' else 'users/criar_user.html'
    return render(request, template_name, {'form': form, 'title': 'Registrar como Empresa' if user_type == 'company' else 'Registrar como Usuário Comum'})

