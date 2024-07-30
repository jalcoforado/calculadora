# Generated by Django 5.0.6 on 2024-07-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCalculadora', '0004_recursodatacenter_custo_total_aplicado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recursodatacenter',
            name='custo_total_aplicado',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='recursodatacenter',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
