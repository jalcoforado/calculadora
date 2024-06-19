from cmath import e
from django import forms
from .models import ComportamentoCusto, Custo, TipoCusto, FuncaoCusto
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