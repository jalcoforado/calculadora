# Generated by Django 5.0.6 on 2024-07-25 16:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComportamentoCusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('exemplos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustoDataCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('DataCenter1', 'Data Center Sefin'), ('DataCenter2', 'Data Center Sepog')], max_length=50)),
                ('vm_type', models.CharField(choices=[('standard_b1s', 'Standard B1s'), ('standard_d2s_v3', 'Standard D2s v3')], max_length=50)),
                ('num_vms', models.IntegerField()),
                ('os', models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows')], max_length=50)),
                ('storage_type', models.CharField(choices=[('standard_hdd', 'Standard HDD'), ('premium_ssd', 'Premium SSD')], max_length=50)),
                ('disk_size', models.CharField(max_length=50)),
                ('num_disks', models.IntegerField()),
                ('num_ips', models.IntegerField()),
                ('ip_type', models.CharField(choices=[('dynamic', 'Dynamic IP'), ('static', 'Static IP')], max_length=50)),
                ('hours_per_month', models.IntegerField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=255)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FuncaoCusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('exemplos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('detalhes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoCusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do tipo de custo (ex: Pessoal, Energia, Licenças)', max_length=255)),
                ('descricao', models.TextField(help_text='Descrição do tipo de custo')),
            ],
        ),
        migrations.CreateModel(
            name='TipoRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Custo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('comportamento_custo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='custos', to='AppCalculadora.comportamentocusto')),
                ('funcao_custo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='custos', to='AppCalculadora.funcaocusto')),
                ('tipo_custo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='custos', to='AppCalculadora.tipocusto')),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaCusto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12)),
                ('periodicidade', models.CharField(choices=[('mensal', 'Mensal'), ('anual', 'Anual')], default='anual', max_length=255)),
                ('data_inicio', models.DateField(default=datetime.date.today)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('custo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='AppCalculadora.custo')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='empresa_custos', to='AppCalculadora.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoDataCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Valor Anual')),
                ('detalhe', models.CharField(max_length=255, verbose_name='Unidade de Medida')),
                ('empresa', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Empresa', to='AppCalculadora.empresa')),
                ('recurso', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Recurso', to='AppCalculadora.recurso')),
            ],
        ),
        migrations.CreateModel(
            name='ServicoRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalculadora.recurso')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalculadora.servico')),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='recursos',
            field=models.ManyToManyField(through='AppCalculadora.ServicoRecurso', to='AppCalculadora.recurso'),
        ),
        migrations.AddField(
            model_name='recurso',
            name='tipo_recurso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCalculadora.tiporecurso'),
        ),
    ]
