from django import forms
from .models import CentroColeta

class CentroColetaForm(forms.ModelForm):
    class Meta:
        model = CentroColeta
        fields = ['nome', 'endereco', 'telefone', 'horario_funcionamento']

    def clean(self):
        cleaned_data = super().clean()
        # Adicione qualquer validacao especifica que voce precisar aqui
        return cleaned_data
