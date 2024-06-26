# Generated by Django 5.0.6 on 2024-06-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCalculadora', '0005_remove_custo_data_fim_remove_custo_data_inicio_and_more'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='empresa',
            name='website',
            field=models.CharField(max_length=255),
        ),
    ]
