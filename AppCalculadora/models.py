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
    tipo_recurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    detalhes = models.TextField()

    def __str__(self):
        return f'{self.tipo_recurso.nome} - {self.descricao}'

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    recursos = models.ManyToManyField(Recurso, through='ServicoRecurso')
     

    def __str__(self):
        return self.nome

class ServicoRecurso(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

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
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    custo = models.ForeignKey(Custo, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=12, decimal_places=2) 
    periodicidade = models.CharField(default="mensal", max_length=255, choices=[('diário', 'Diário'), ('mensal', 'Mensal'), ('anual', 'Anual')])
    data_inicio = models.DateField(default=datetime.date.today)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
       return f"{self.empresa.nome} - {self.custo}"
