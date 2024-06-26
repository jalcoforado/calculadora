# Generated by Django 5.0.6 on 2024-05-14 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCalculadora', '0004_empresa_remove_custo_valor_empresacusto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custo',
            name='data_fim',
        ),
        migrations.RemoveField(
            model_name='custo',
            name='data_inicio',
        ),
        migrations.AddField(
            model_name='empresacusto',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='empresacusto',
            name='data_inicio',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='empresacusto',
            name='periodicidade',
            field=models.CharField(choices=[('diário', 'Diário'), ('mensal', 'Mensal'), ('anual', 'Anual')], default='mensal', max_length=255),
        ),
    ]
