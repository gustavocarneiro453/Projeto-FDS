from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreateForm(UserCreationForm):
    """
    Formulário personalizado para criação de usuários comuns.
    """
    email = forms.EmailField(required=True, help_text="Endereço de e-mail válido.")

    class Meta:
        model = User
        fields = (
            'nome',
            'sobrenome',
            'email',
            'telefone',
            'password1',
            'password2',
        )
    
    usable_password = None
    
    def clean(self):
        """
        Validação adicional para campos específicos.
        """
        cleaned_data = super().clean()
        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

class UserCompanyCreateForm(UserCreationForm):
    """
    Formulário personalizado para criação de empresas.
    """
    email = forms.EmailField(required=True, help_text="Endereço de e-mail válido.")

    class Meta:
        model = User
        fields = (
            'nome_empresa',
            'email',
            'endereco_empresa',
            'telefone_empresa',
            'password1',
            'password2',
        )
    
    usable_password = None

    def clean(self):
        """
        Validação adicional para campos específicos.
        """
        cleaned_data = super().clean()
        required_fields = ['nome_empresa', 'endereco_empresa', 'telefone_empresa', 'password1']

        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Este campo é obrigatório para empresas.")

        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email