# Generated by Django 5.1.1 on 2024-09-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centrocoleta',
            name='horario_funcionamento',
        ),
        migrations.AddField(
            model_name='centrocoleta',
            name='cep',
            field=models.CharField(blank=True, help_text='Número do CEP', max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='centrocoleta',
            name='complemento',
            field=models.CharField(blank=True, help_text='Complemento do endereço', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='centrocoleta',
            name='horario_abertura',
            field=models.CharField(blank=True, help_text='Horário de abertura.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='centrocoleta',
            name='horario_fechamento',
            field=models.CharField(blank=True, help_text='Horário de fechamento.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='centrocoleta',
            name='numero',
            field=models.CharField(blank=True, help_text='Número do endereço do centro', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='centrocoleta',
            name='tipos',
            field=models.CharField(blank=True, choices=[('metal', 'Metal'), ('papel', 'Papel'), ('plastico', 'Plástico'), ('organico', 'Orgânico'), ('perigoso', 'Perigoso'), ('vidro', 'Vidro')], max_length=255, null=True),
        ),
    ]
