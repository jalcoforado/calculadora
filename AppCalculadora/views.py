from django.core.paginator import Paginator
from decimal import Decimal, InvalidOperation
from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from AppCalculadora.form import ComportamentoCustoForm, CustoForm, DataCenterCostForm, EmpresaCustoForm, EmpresaForm, FuncaoCustoForm, ModeloAssinaturaForm, RecursoDataCenterForm, ServicoRecursoForm,  TipoCustoForm, TipoRecursoForm, RecursoForm, ServicoForm, ServicoRecursoInlineFormSet
from django.contrib import messages
from AppCalculadora.models  import ComportamentoCusto, Custo, CustoDataCenter, EmpresaCusto, ModeloAssinatura, RecursoDataCenter, TipoCusto, TipoRecurso, Recurso, Servico
from AppCalculadora.models  import Empresa, FuncaoCusto, ServicoRecurso
from django.db.models import RestrictedError


def home(request):
    return render(request, 'home.html')

def listar_empresa(request):
    empresas = Empresa.objects.all()  # Obtenha todas as empresas
    context = {
        'empresas': empresas  # Passe as empresas para o contexto
    }
    return render(request, 'empresa/listar_empresa.html', context)


# Funções do Empresa 
def cadastrar_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro cadastrado com sucesso!')
            return redirect('listarEmpresa')  # Redirecione para a lista de empresas após o cadastro
    else:
        form = EmpresaForm()
    return render(request, 'empresa/cadastrar_empresa.html', {'form': form})

def editar_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro atualizado com sucesso!')
            return redirect('listarEmpresa')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresa/editar_empresa.html', {'form': form})

def excluir_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        try:
            empresa.delete()
            messages.success(request, 'Registro excluído com sucesso!')
        except RestrictedError:  
                messages.error(request, 'Não é possível excluir esta empresa porque ela está sendo referenciada por um custo.')
        return redirect('listarEmpresa')
    return render(request, 'empresa/excluir_empresa.html', {'empresa': empresa})

# Funções do Tipo de Recurso 

def listar_tipo_recurso(request):
    tipos_recurso = TipoRecurso.objects.all()
    return render(request, 'tiporecurso/listar_tipo_recurso.html', {'tipos_recurso': tipos_recurso})

def cadastrar_tipo_recurso(request):
    if request.method == 'POST':
        form = TipoRecursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de Recurso cadastrado com sucesso!')
            return redirect('listarTipoRecurso')
    else:
        form = TipoRecursoForm()
    return render(request, 'tiporecurso/cadastrar_tipo_recurso.html', {'form': form})

def editar_tipo_recurso(request, pk):
    tipo_recurso = get_object_or_404(TipoRecurso, pk=pk)
    if request.method == 'POST':
        form = TipoRecursoForm(request.POST, instance=tipo_recurso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de Recurso atualizado com sucesso!')
            return redirect('listarTipoRecurso')
    else:
        form = TipoRecursoForm(instance=tipo_recurso)
    return render(request, 'tiporecurso/editar_tipo_recurso.html', {'form': form})

def excluir_tipo_recurso(request, pk):
    tipo_recurso = get_object_or_404(TipoRecurso, pk=pk)
    if request.method == 'POST':
        tipo_recurso.delete()
        messages.success(request, 'Tipo de Recurso excluído com sucesso!')
        return redirect('listarTipoRecurso')
    return render(request, 'tiporecurso/excluir_tipo_recurso.html', {'tipo_recurso': tipo_recurso})


# Funções Recurso 

def listar_recurso(request):
    recursos = Recurso.objects.all()
    return render(request, 'recurso/listar_recurso.html', {'recursos': recursos})

def cadastrar_recurso(request):
    if request.method == 'POST':
        form = RecursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recurso cadastrado com sucesso!')
            return redirect('listarRecurso')
    else:
        form = RecursoForm()
    return render(request, 'recurso/cadastrar_recurso.html', {'form': form})

def editar_recurso(request, pk):
    recurso = get_object_or_404(Recurso, pk=pk)
    if request.method == 'POST':
        form = RecursoForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recurso atualizado com sucesso!')
            return redirect('listarRecurso')
    else:
        form = RecursoForm(instance=recurso)
    return render(request, 'recurso/editar_recurso.html', {'form': form})

def excluir_recurso(request, pk):
    recurso = get_object_or_404(Recurso, pk=pk)
    if request.method == 'POST':
        recurso.delete()
        messages.success(request, 'Recurso excluído com sucesso!')
        return redirect('listarRecurso')
    return render(request, 'recurso/excluir_recurso.html', {'recurso': recurso})

# Funções Servico

def listar_servico(request):
    servicos = Servico.objects.all()
    return render(request, 'servico/listar_servico.html', {'servicos': servicos})

def cadastrar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço cadastrado com sucesso!')
            return redirect('listarServico')
    else:
        form = ServicoForm()
    return render(request, 'servico/cadastrar_servico.html', {'form': form})

def editar_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = RecursoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servico atualizado com sucesso!')
            return redirect('listarServico')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'servico/editar_servico.html', {'form': form})

def excluir_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.delete()
        messages.success(request, 'Serviço excluído com sucesso!')
        return redirect('listarServico')
    return render(request, 'servico/excluir_servico.html', {'servico': servico})    


# Funções Tipo Custo
def listar_tipo_custo(request):
    tipos_custo = TipoCusto.objects.all()
    return render(request, 'tipocusto/listar_tipo_custo.html', {'tipos_custo': tipos_custo})

def cadastrar_tipo_custo(request):
    if request.method == 'POST':
        form = TipoCustoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de Custo cadastrado com sucesso!')
            return redirect('listarTipoCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = TipoCustoForm()
    return render(request, 'tipocusto/cadastrar_tipo_custo.html', {'form': form})

def editar_tipo_custo(request, pk):
    tipo_custo = get_object_or_404(TipoCusto, pk=pk)
    if request.method == 'POST':
        form = TipoCustoForm(request.POST, instance=tipo_custo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de Custo atualizado com sucesso!')
            return redirect('listarTipoCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = TipoCustoForm(instance=tipo_custo)
    return render(request, 'tipocusto/editar_tipo_custo.html', {'form': form})

def excluir_tipo_custo(request, pk):
    tipo_custo = get_object_or_404(TipoCusto, pk=pk)
    if request.method == 'POST':
        tipo_custo.delete()
        messages.success(request, 'Tipo de Custo excluído com sucesso!')
        return redirect('listarTipoCusto')
    return render(request, 'tipocusto/excluir_tipo_custo.html', {'tipo_custo': tipo_custo})


# Funções Função Custo
def listar_funcao_custo(request):
    funcoes_custo = FuncaoCusto.objects.all()
    return render(request, 'funcaocusto/listar_funcao_custo.html', {'funcoes_custo': funcoes_custo})

def cadastrar_funcao_custo(request):
    if request.method == 'POST':
        form = FuncaoCustoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Função de Custo cadastrada com sucesso!')
            return redirect('listarFuncaoCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = FuncaoCustoForm()
    return render(request, 'funcaocusto/cadastrar_funcao_custo.html', {'form': form})

def editar_funcao_custo(request, pk):
    funcao_custo = get_object_or_404(FuncaoCusto, pk=pk)
    if request.method == 'POST':
        form = FuncaoCustoForm(request.POST, instance=funcao_custo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Função de Custo atualizada com sucesso!')
            return redirect('listarFuncaoCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = FuncaoCustoForm(instance=funcao_custo)
    return render(request, 'funcaocusto/editar_funcao_custo.html', {'form': form})

def excluir_funcao_custo(request, pk):
    funcao_custo = get_object_or_404(FuncaoCusto, pk=pk)
    if request.method == 'POST':
        funcao_custo.delete()
        messages.success(request, 'Função de Custo excluída com sucesso!')
        return redirect('listarFuncaoCusto')
    return render(request, 'funcaocusto/excluir_funcao_custo.html', {'funcao_custo': funcao_custo})

# Funções Comportamento Custo

def listar_comportamento_custo(request):
    comportamentos_custo = ComportamentoCusto.objects.all()
    return render(request, 'comportamentocusto/listar_comportamento_custo.html', {'comportamentos_custo': comportamentos_custo})

def cadastrar_comportamento_custo(request):
    if request.method == 'POST':
        form = ComportamentoCustoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comportamento de Custo cadastrado com sucesso!')
            return redirect('listarComportamentoCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = ComportamentoCustoForm()
    return render(request, 'comportamentocusto/cadastrar_comportamento_custo.html', {'form': form})

def editar_comportamento_custo(request, pk):
    comportamento_custo = get_object_or_404(ComportamentoCusto, pk=pk)
    if request.method == 'POST':
        form = ComportamentoCustoForm(request.POST, instance=comportamento_custo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comportamento de Custo atualizado com sucesso!')
            return redirect('listarComportamentoCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = ComportamentoCustoForm(instance=comportamento_custo)
    return render(request, 'comportamentocusto/editar_comportamento_custo.html', {'form': form})

def excluir_comportamento_custo(request, pk):
    comportamento_custo = get_object_or_404(ComportamentoCusto, pk=pk)
    if request.method == 'POST':
        comportamento_custo.delete()
        messages.success(request, 'Comportamento de Custo excluído com sucesso!')
        return redirect('listarComportamentoCusto')
    return render(request, 'comportamentocusto/excluir_comportamento_custo.html', {'comportamento_custo': comportamento_custo})

# Funções Custo
def listar_custo(request):
    custos = Custo.objects.all()
    return render(request, 'custo/listar_custo.html', {'custos': custos})

def cadastrar_custo(request):
    if request.method == 'POST':
        form = CustoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Custo cadastrado com sucesso!')
            return redirect('listarCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = CustoForm()
    return render(request, 'custo/cadastrar_custo.html', {'form': form})

def editar_custo(request, pk):
    custo = get_object_or_404(Custo, pk=pk)
    if request.method == 'POST':
        form = CustoForm(request.POST, instance=custo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Custo atualizado com sucesso!')
            return redirect('listarCusto')
        else:
            messages.error(request, 'Erro ao validar o formulário. Verifique os dados e tente novamente.')
    else:
        form = CustoForm(instance=custo)
    return render(request, 'custo/editar_custo.html', {'form': form})

def excluir_custo(request, pk):
    custo = get_object_or_404(Custo, pk=pk)
    if request.method == 'POST':
        custo.delete()
        messages.success(request, 'Custo excluído com sucesso!')
        return redirect('listarCusto')
    return render(request, 'custo/excluir_custo.html', {'custo': custo})


# Funções Calculadora
def calcular_custo_datacenter(request):
    if request.method == 'POST':
        form = DataCenterCostForm(request.POST)
        if form.is_valid():
            region = form.cleaned_data['region']
            vm_type = form.cleaned_data['vm_type']
            num_vms = form.cleaned_data['num_vms']
            os = form.cleaned_data['os']
            storage_type = form.cleaned_data['storage_type']
            disk_size = form.cleaned_data['disk_size']
            num_disks = form.cleaned_data['num_disks']
            num_ips = form.cleaned_data['num_ips']
            ip_type = form.cleaned_data['ip_type']
            hours_per_month = form.cleaned_data['hours_per_month']
            
            # Simulação de cálculo de custo
            base_cost_per_hour = {
                'standard_b1s': 0.02,
                'standard_d2s_v3': 0.10,
                # Adicione outros tipos de VM e seus custos aqui
            }
            
            storage_cost_per_gb = {
                'standard_hdd': 0.001,
                'premium_ssd': 0.002,
                # Adicione outros tipos de armazenamento e seus custos aqui
            }
            
            ip_cost_per_hour = {
                'dynamic': 0.003,
                'static': 0.005,
                # Adicione outros tipos de IP e seus custos aqui
            }
            
            cost_per_hour = base_cost_per_hour.get(vm_type, 0)
            storage_cost = storage_cost_per_gb.get(storage_type, 0) * int(disk_size)
            ip_cost = ip_cost_per_hour.get(ip_type, 0)
            
            total_vm_cost = cost_per_hour * num_vms * hours_per_month
            total_storage_cost = storage_cost * num_disks 


# Funções Empresa Custo
def cadastrar_empresa_custo(request):
    if request.method == 'POST':
        form = EmpresaCustoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarEmpresaCusto')
        else:
            print(form.errors, form.error_class)
    else:
        form = EmpresaCustoForm()
    
    return render(request, 'empresacusto/cadastrar_empresa_custo.html', {'form': form})


def listar_empresa_custo(request):
    empresa_id = request.GET.get('empresa')
    if empresa_id:
        empresacustos = EmpresaCusto.objects.filter(empresa_id=empresa_id)
    else:
        empresacustos = EmpresaCusto.objects.all()

    empresas = Empresa.objects.all()

    return render(request, 'empresacusto/listar_empresa_custo.html', {
        'empresacustos': empresacustos,
        'empresas': empresas,
    })


def editar_empresa_custo(request, pk):
    empresacusto = get_object_or_404(EmpresaCusto, pk=pk)
    if request.method == 'POST':
        form = EmpresaCustoForm(request.POST, instance= empresacusto)
        if form.is_valid():
            form.save()
            return redirect('listarEmpresaCusto')
    else:
        form = EmpresaCustoForm(instance=empresacusto)
    
    return render(request, 'empresacusto/editar_empresa_custo.html', {'form': form, 'empresacusto': empresacusto})

def excluir_empresa_custo(request, pk):
    empresacusto = get_object_or_404(EmpresaCusto, pk=pk)
    if request.method == 'POST':
        try:
            empresacusto.delete()
            messages.success(request, 'Empresa excluída com sucesso.')
        except RestrictedError:
            messages.error(request, 'Não é possível excluir esta empresa porque ela está sendo referenciada por um custo.')
        return redirect('listarEmpresaCusto')
    return render(request, 'empresacusto/excluir_empresa_custo.html', {'empresacusto': empresacusto})



# 2 passo do modelo 
def calcular_custos(empresa, percentual_finops, valor):
    try:
        # Calcular o somatório do campo valor para todos os registros da mesma empresa
        total_valor = EmpresaCusto.objects.filter(empresa=empresa).aggregate(total=models.Sum('valor'))['total'] or Decimal('0.00')
        
        # Certificar que total_valor e percentual_finops são do tipo Decimal
        total_valor = Decimal(total_valor)
        percentual_finops = Decimal(percentual_finops)
        custo_total = (total_valor * percentual_finops) / 100
        
        # Calcular o custo_total_aplicado e unitário
        custo_total_aplicado = custo_total
        valor_unitario = (custo_total / valor)
        
        return custo_total_aplicado, valor_unitario
    except InvalidOperation:
        # Tratar a exceção de operação inválida
        return Decimal('0.00'), Decimal('0.00')

def listar_recurso_datacenter(request):
    empresa_id = request.GET.get('empresa')
    if empresa_id:
        recursosDataCenter = RecursoDataCenter.objects.filter(empresa__id=empresa_id)
    else:
        recursosDataCenter = RecursoDataCenter.objects.all()
    return render(request, 'recursodatacenter/listar_recurso_datacenter.html', {'recursosDataCenter': recursosDataCenter})

def cadastrar_recurso_datacenter(request):
    if request.method == 'POST':
        form = RecursoDataCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarRecursoDatacenter')
    else:
        form = RecursoDataCenterForm()
    return render(request, 'recursodatacenter/cadastrar_recurso_datacenter.html', {'form': form})

def editar_recurso_datacenter(request, pk):
    recursosDataCenter = get_object_or_404(RecursoDataCenter, pk=pk)
    if request.method == 'POST':
        form = RecursoDataCenterForm(request.POST, instance=recursosDataCenter)
        if form.is_valid():
            form.save()
            return redirect('listarRecursoDatacenter')
    else:
        form = RecursoDataCenterForm(instance=recursosDataCenter)
    return render(request, 'recursodatacenter/editar_recurso_datacenter.html', {'form': form})



def excluir_recurso_datacenter(request, pk):
    recursoDataCenter = get_object_or_404(RecursoDataCenter, pk=pk)
    if request.method == 'POST':
        recursoDataCenter.delete()
        return redirect('listarRecursoDatacenter')
    return render(request, 'recursodatacenter/excluir_recurso_datacenter.html', {'recursoDataCenter': recursoDataCenter})


# servico recurso
def cadastrar_servico_recurso(request):
    if request.method == 'POST':
        servico_form = ServicoForm(request.POST)        
        servico_recurso_formset = ServicoRecursoInlineFormSet(request.POST)        
        if servico_form.is_valid() and servico_recurso_formset.is_valid():
            servico = servico_form.save()
            servico_recursos = servico_recurso_formset.save(commit=False)
            for servico_recurso in servico_recursos:
                servico_recurso.servico = servico
                servico_recurso.save()
            return redirect('listarServicoRecurso')
    else:
        servico_form = ServicoForm()
        servico_recurso_formset = ServicoRecursoInlineFormSet()
    return render(request, 'servicorecurso/cadastrar_servico_recurso.html', {
        'servico_form': servico_form,
        'servico_recurso_formset': servico_recurso_formset,
    })



def listar_servico_recurso(request):
    servicos_recursos = ServicoRecurso.objects.all()
    paginator = Paginator(servicos_recursos, 10)  # Mostra 10 recursos por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'servicorecurso/listar_servico_recurso.html', {'page_obj': page_obj})


def editar_servico_recurso(request, id):    
    servico_recurso = get_object_or_404(ServicoRecurso, id=id)
    if request.method == 'POST':
        form = ServicoRecursoForm(request.POST, instance=servico_recurso)
        if form.is_valid():
            form.save()
            return redirect(reverse('listar_servico_recurso'))
    else:
        form = ServicoRecursoForm(instance=servico_recurso)
    return render(request, 'servicorecurso/editar_servico_recurso.html', {'form': form, 'servicorecurso': servico_recurso})

def excluir_servico_recurso(request, id):
    servico_recurso = get_object_or_404(ServicoRecurso, id=id)
    if request.method == 'POST':
        servico_recurso.delete()
        return redirect(reverse('listar_servico_recurso'))
    return render(request, 'servicorecurso/excluir_servico_recurso.html', {'servicorecurso': servico_recurso})

# Modelo Assinatura
def cadastrar_modelo_assinatura(request):
    if request.method == 'POST':
        form = ModeloAssinaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarModeloAssinatura')
    else:
        form = ModeloAssinaturaForm()
    
    return render(request, 'modeloassinatura/cadastrar_modelo_assinatura.html', {'form': form})

def listar_modelo_assinatura(request):
    modelos = ModeloAssinatura.objects.all()
    return render(request, 'modeloassinatura/listar_modelo_assinatura.html', {'modelos': modelos})

def editar_modelo_assinatura(request, pk):
    modelo = get_object_or_404(ModeloAssinatura, pk=pk)
    if request.method == 'POST':
        form = ModeloAssinaturaForm(request.POST, instance=modelo)
        if form.is_valid():
            form.save()
            return redirect('listarModeloAssinatura')
    else:
        form = ModeloAssinaturaForm(instance=modelo)
    
    return render(request, 'modeloassinatura/editar_modelo_assinatura.html', {'form': form})

def excluir_modelo_assinatura(request, pk):
    modelo = get_object_or_404(ModeloAssinatura, pk=pk)
    if request.method == 'POST':
        modelo.delete()
        return redirect('listarModeloAssinatura')
    return render(request, 'modeloassinatura/excluir_modelo_assinatura.html', {'modelo': modelo})