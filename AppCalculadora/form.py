from cmath import e
from datetime import date
from django import forms
from .models import ComportamentoCusto, Custo, CustoDataCenter, EmpresaCusto, TipoCusto, FuncaoCusto
from .models import Empresa, TipoRecurso, Recurso, Servico, ServicoRecurso


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'endereco', 'telefone', 'email', 'website']

class TipoRecursoForm(forms.ModelForm):
    class Meta:
        model = TipoRecurso
        fields = ['nome']        


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['tipo_recurso', 'descricao', 'detalhes']

class ServicoRecursoForm(forms.ModelForm):
    class Meta:
        model = ServicoRecurso
        fields = ['recurso', 'quantidade']
        widgets = {
            'recurso': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }       

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao']

class TipoCustoForm(forms.ModelForm):
    class Meta:
        model = TipoCusto
        fields = ['nome', 'descricao']

class FuncaoCustoForm(forms.ModelForm):
    class Meta:
        model = FuncaoCusto
        fields = ['nome', 'exemplos']        

class ComportamentoCustoForm(forms.ModelForm):
    class Meta:
        model = ComportamentoCusto
        fields = ['nome', 'exemplos']   

class CustoForm(forms.ModelForm):
    class Meta:
        model = Custo
        fields = ['descricao', 'tipo_custo', 'funcao_custo', 'comportamento_custo']       

class DataCenterCostForm(forms.ModelForm):
    INSTANCE_SERIES_CHOICES = [
        ('basic', 'Básico'),
        ('standard', 'Padrão'),
        ('premium', 'Premium'),
    ]
    CONTRACT_TYPE_CHOICES = [
        ('on_demand', 'Por Demanda'),
        ('reserved', 'Reservado'),
    ]

    instance_series = forms.ChoiceField(choices=INSTANCE_SERIES_CHOICES, label="Série de Instâncias", widget=forms.Select(attrs={'class': 'form-control'}))
    contract_type = forms.ChoiceField(choices=CONTRACT_TYPE_CHOICES, label="Forma de Contrato", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustoDataCenter
        fields = ['region', 'vm_type', 'num_vms', 'os', 'storage_type', 'disk_size', 'num_disks', 'num_ips', 'ip_type', 'hours_per_month', 'instance_series', 'contract_type']
        widgets = {
            'region': forms.Select(attrs={'class': 'form-control'}),
            'vm_type': forms.Select(attrs={'class': 'form-control'}),
            'num_vms': forms.NumberInput(attrs={'class': 'form-control'}),
            'os': forms.Select(attrs={'class': 'form-control'}),
            'storage_type': forms.Select(attrs={'class': 'form-control'}),
            'disk_size': forms.NumberInput(attrs={'class': 'form-control'}),  # Changed to NumberInput if it suits the model
            'num_disks': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_ips': forms.NumberInput(attrs={'class': 'form-control'}),
            'ip_type': forms.Select(attrs={'class': 'form-control'}),
            'hours_per_month': forms.NumberInput(attrs={'class': 'form-control'}),
        }           
        

class EmpresaCustoForm(forms.ModelForm):
    data_inicio = forms.DateField(initial=date(date.today().year, 1, 1))
    data_fim = forms.DateField(initial=date(date.today().year, 12, 31))
    class Meta:
        model = EmpresaCusto
        fields = ['empresa', 'custo', 'valor', 'periodicidade', 'data_inicio', 'data_fim']
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'custo': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'periodicidade': forms.Select(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
        }   
         


        