from decimal import Decimal, InvalidOperation
from django.db import models

# Create your models here.
from django.db import models
import datetime

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    

class TipoRecurso(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Recurso(models.Model):
        
    UNIDADE_MEDIDA_CHOICES = [
        ('horas de CPU ANO', 'horas de CPU ANO'),
        ('em gigabytes (GB) por mês', 'em gigabytes (GB) por mês'),
        ('em gigabytes (GB) Transferidos por mês', 'em gigabytes (GB) Transferidos por mês'),
        ('eventos monitorados por mês', 'eventos monitorados por mês'),        
    ]
    tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    detalhes = models.TextField()
    unidade_medida = models.CharField(
        max_length=255,
        choices=UNIDADE_MEDIDA_CHOICES,
        default='horas de CPU ANO',
    )

    def __str__(self):
        return f'{self.tipo_recurso} - {self.descricao}'

        

class Servico(models.Model):
    IAAS = 'IAAS'
    PAAS = 'PAAS'
    SAAS = 'SAAS'
    
    MODELO_CHOICES = [
        (IAAS, 'Infrastructure as a Service (IAAS)'),
        (PAAS, 'Platform as a Service (PAAS)'),
        (SAAS, 'Software as a Service (SAAS)'),
    ]
    
    modelo = models.CharField(
        max_length=255,
        choices=MODELO_CHOICES,
        default=IAAS,
    )
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
class ServicoRecurso(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)   
    detalhe = models.CharField(max_length=80, default="Nada a informar")

    def __str__(self):
        return f'{self.servico.nome} usa {self.quantidade} {self.recurso.descricao}'
    

class TipoCusto(models.Model):
    nome = models.CharField(max_length=255, help_text="Nome do tipo de custo (ex: Pessoal, Energia, Licenças)")
    descricao = models.TextField(help_text="Descrição do tipo de custo")

    def __str__(self):
        return self.nome

class FuncaoCusto(models.Model):
    nome = models.CharField(max_length=255)
    exemplos = models.TextField()

    def __str__(self):
        return self.nome

class ComportamentoCusto(models.Model):
    nome = models.CharField(max_length=255)
    exemplos = models.TextField()

    def __str__(self):
        return self.nome

class Custo(models.Model):
    descricao = models.CharField(max_length=255)
    tipo_custo = models.ForeignKey(TipoCusto, on_delete=models.CASCADE, related_name="custos", default=1)
    funcao_custo = models.ForeignKey(FuncaoCusto, on_delete=models.CASCADE, related_name="custos", default=1)
    comportamento_custo = models.ForeignKey(ComportamentoCusto, on_delete=models.CASCADE, related_name="custos", default=1)  # assumindo que existe um ComportamentoCusto com ID 1

    def __str__(self):
        return f"{self.descricao}"

class EmpresaCusto(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.RESTRICT, related_name="empresa_custos")
    custo = models.ForeignKey(Custo, on_delete=models.RESTRICT)
    valor = models.DecimalField(max_digits=12, decimal_places=2) 
    periodicidade = models.CharField(default="anual", max_length=255, choices=[('mensal', 'Mensal'), ('anual', 'Anual')])
    data_inicio = models.DateField(default=datetime.date.today)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
       return f"{self.empresa.nome} - {self.custo}"



class CustoDataCenter(models.Model):
    REGION_CHOICES = [
        ('DataCenter1', 'Data Center Sefin'),
        ('DataCenter2', 'Data Center Sepog'),
    ]
    
    VM_TYPE_CHOICES = [
        ('standard_b1s', 'Standard B1s'),
        ('standard_d2s_v3', 'Standard D2s v3'),
        # Adicione outros tipos de VM aqui
    ]
    
    OS_CHOICES = [
        ('linux', 'Linux'),
        ('windows', 'Windows'),
    ]
    
    STORAGE_TYPE_CHOICES = [
        ('standard_hdd', 'Standard HDD'),
        ('premium_ssd', 'Premium SSD'),
    ]
    
    IP_TYPE_CHOICES = [
        ('dynamic', 'Dynamic IP'),
        ('static', 'Static IP'),
    ]

    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    vm_type = models.CharField(max_length=50, choices=VM_TYPE_CHOICES)
    num_vms = models.IntegerField()
    os = models.CharField(max_length=50, choices=OS_CHOICES)
    storage_type = models.CharField(max_length=50, choices=STORAGE_TYPE_CHOICES)
    disk_size = models.CharField(max_length=50)
    num_disks = models.IntegerField()
    num_ips = models.IntegerField()
    ip_type = models.CharField(max_length=50, choices=IP_TYPE_CHOICES)
    hours_per_month = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.vm_type} - {self.region} - {self.total_cost}"



# 2 Passo da metodologia

 
class RecursoDataCenter(models.Model):
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE, related_name='Empresa', null=True, blank=True, default=None)
    recurso = models.ForeignKey('Recurso', on_delete=models.CASCADE, related_name='Recurso', null=True, blank=True, default=None)    
    valor = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Valor Anual", default=0.00)
    detalhe = models.CharField(max_length=255, verbose_name="Unidade de Medida")
    percentual_finops = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    custo_total_aplicado = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    valor_unitario = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    def save(self, *args, **kwargs):
        try:
            # Calcular o somatório do campo valor para todos os registros da mesma empresa
            total_valor = EmpresaCusto.objects.filter(empresa=self.empresa).aggregate(total=models.Sum('valor'))['total'] or Decimal('0.00')
            
            # Certificar que total_valor e percentual_finops são do tipo Decimal
            total_valor = Decimal(total_valor)
            percentual_finops = Decimal(self.percentual_finops)
            custo_total = (total_valor * percentual_finops)/100
            # Calcular o custo_total_aplicado e unitário
            self.custo_total_aplicado = custo_total
            self.valor_unitario = (custo_total / self.valor)
        except InvalidOperation:
            # Tratar a exceção de operação inválida
            self.custo_total_aplicado = Decimal('0.00')
        
        # Chamar o método save original
        super(RecursoDataCenter, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.empresa.nome} -  {self.valor} - {self.detalhe}"
    
# 5 Modelo de assinatura
class ModeloAssinatura(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)    
    valor_desconto = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Valor Anual", default=0.00)   

    def __str__(self):
        return f"{self.nome} - {self.valor_desconto}"   

        