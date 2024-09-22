from django.db import models
from users.models import User

class CentroColeta(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome do centro de coleta.")
    endereco = models.CharField(max_length=500, help_text="Endereço do centro de coleta.")
    telefone = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Telefone do centro.")
    horario_funcionamento = models.CharField(max_length=100, help_text="Horário de funcionamento.")
    usuario_responsavel = models.ForeignKey(User, related_name='centros_responsaveis', on_delete=models.CASCADE, help_text="Usuário responsável pelo centro.")

    def __str__(self):
        return self.nome