# Generated by Django 5.1.1 on 2024-09-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centros', '0003_remove_centrocoleta_horario_funcionamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centrocoleta',
            name='tipos',
            field=models.CharField(blank=True, choices=[('metal', 'Metal'), ('papel', 'Papel'), ('plastico', 'Plástico'), ('organico', 'Orgânico'), ('perigoso', 'Perigoso'), ('vidro', 'Vidro')], max_length=50, null=True),
        ),
    ]
