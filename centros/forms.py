from django import forms
from .models import CentroColeta

class CentroColetaForm(forms.ModelForm):
    TIPOS_CHOICES = [
        ('metal', 'Metal'),
        ('papel', 'Papel'),
        ('plastico', 'Plástico'),
        ('organico', 'Orgânico'),
        ('perigoso', 'Perigoso'),
        ('vidro', 'Vidro')
    ]
    
    tipos = forms.MultipleChoiceField(
        choices=TIPOS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Tipos de Materiais"
    )

    class Meta:
        model = CentroColeta
        fields = ['nome', 'telefone', 'endereco', 'numero', 'complemento', 'cep', 'tipos', 'horario_abertura', 'horario_fechamento', 'usuario_responsavel']
    
    def clean_tipos(self):
        tipos = self.cleaned_data.get('tipos')
        # Adicione qualquer validacao especifica que voce precisar aqui
        return ','.join(tipos)
