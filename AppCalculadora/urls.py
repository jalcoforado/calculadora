from django.urls import path
from AppCalculadora.views import home
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    
    
    # Módulo de Empresa
    path('listarempresa/', views.listar_empresa, name='listarEmpresa'),
    path('cadastrarempresa/', views.cadastrar_empresa, name='cadastrarEmpresa'),
    path('editarempresa/<int:pk>/', views.editar_empresa, name='editarEmpresa'),
    path('excluirempresa/<int:pk>/', views.excluir_empresa, name='excluirEmpresa'),
    
    # Módulo Tipo de Recurso
    path('listartiporecurso/', views.listar_tipo_recurso, name='listarTipoRecurso'),
    path('cadastrartiporecurso/', views.cadastrar_tipo_recurso, name='cadastrarTipoRecurso'),
    path('editartiporecurso/<int:pk>/', views.editar_tipo_recurso, name='editarTipoRecurso'),
    path('excluirtiporecurso/<int:pk>/', views.excluir_tipo_recurso, name='excluirTipoRecurso'),

    # Módulo Recurso
    path('listarrecurso/', views.listar_recurso, name='listarRecurso'),
    path('cadastrarrecurso/', views.cadastrar_recurso, name='cadastrarRecurso'),
    path('editarrecurso/<int:pk>/', views.editar_recurso, name='editarRecurso'),
    path('excluirrecurso/<int:pk>/', views.excluir_recurso, name='excluirRecurso'),

    
   # Módulo Tipo de Custo
    path('listartipocusto/', views.listar_tipo_custo, name='listarTipoCusto'),
    path('cadastrartipocusto/', views.cadastrar_tipo_custo, name='cadastrarTipoCusto'),
    path('editartipocusto/<int:pk>/', views.editar_tipo_custo, name='editarTipoCusto'),
    path('excluirtipocusto/<int:pk>/', views.excluir_tipo_custo, name='excluirTipoCusto'),
    
    # Módulo Função de Custo

    path('listarfuncaodecusto/', views.listar_funcao_custo, name='listarFuncaoCusto'),
    path('cadastrarfuncaodecusto/', views.cadastrar_funcao_custo, name='cadastrarFuncaoCusto'),
    path('editarfuncaodecusto/<int:pk>/', views.editar_funcao_custo, name='editarFuncaoCusto'),
    path('excluirfuncaodecusto/<int:pk>/', views.excluir_funcao_custo, name='excluirFuncaoCusto'),

    # Módulo Comportamento de Custo
    path('listarcomportamentocusto/', views.listar_comportamento_custo, name='listarComportamentoCusto'),
    path('cadastrarcomportamentocusto/', views.cadastrar_comportamento_custo, name='cadastrarComportamentoCusto'),
    path('editarcomportamentocusto/<int:pk>/', views.editar_comportamento_custo, name='editarComportamentoCusto'),
    path('excluircomportamentocusto/<int:pk>/', views.excluir_comportamento_custo, name='excluirComportamentoCusto'),

    # Módulo Custo
    path('listarcusto/', views.listar_custo, name='listarCusto'),
    path('cadastrarcusto/', views.cadastrar_custo, name='cadastrarCusto'),
    path('editarcusto/<int:pk>/', views.editar_custo, name='editarCusto'),
    path('excluircusto/<int:pk>/', views.excluir_custo, name='excluirCusto'), 

    # Módulo Empresa Custo   
    path('cadastrarempresacusto/', views.cadastrar_empresa_custo, name='cadastrarEmpresaCusto'),
    path('listarempresacusto/', views.listar_empresa_custo, name='listarEmpresaCusto'),
    path('editarempresacusto/<int:pk>/', views.editar_empresa_custo, name='editarEmpresaCusto'),
    path('excluirempresacusto/<int:pk>/', views.excluir_empresa_custo, name='excluirEmpresaCusto'),

    # Módulo Calculo do Custo
    path('calcularcusto/', views.calcular_custo_datacenter, name='calcularCustoDatacenter'),
    #
    path('calcularpreco/', views.calcular_preco, name='calcularPreco'),
    path('listarcalcularcusto/', views.listar_calcular_custo, name='listarCalcularCusto'),
    # Outras URLs
    
    # Passo 2 Cadastrar recurso datacenter
    path('listarecursodatacenter/', views.listar_recurso_datacenter, name='listarRecursoDatacenter'),
    path('cadastrarrecursodatacenter/', views.cadastrar_recurso_datacenter, name='cadastrarRecursoDatacenter'),
    path('editarrecursodatacenter/<int:pk>/', views.editar_recurso_datacenter, name='editarRecursoDatacenter'),
    path('excluirrecursodatacenter/<int:pk>/', views.excluir_recurso_datacenter, name='excluirRecursoDatacenter'), 

     # Módulo Servico
    path('listarservico/', views.listar_servico, name='listarServico'),
    path('cadastrarservico/', views.cadastrar_servico, name='cadastrarServico'),
    path('editarservico/<int:pk>/', views.editar_servico, name='editarServico'),
    path('excluirservico/<int:pk>/', views.excluir_servico, name='excluirServico'),    


    # Passo 4 ServicoRecurso    
    path('listarservicorecurso', views.listar_servico_recurso, name='listarServicoRecurso'),
    path('cadastrarservicorecurso/', views.cadastrar_servico_recurso, name='cadastrarServicoRecurso'),
    path('editarservicorecurso/<int:id>/', views.editar_servico_recurso, name='editarServicoRecurso'),
    path('excluirservicorecurso/<int:id>/', views.excluir_servico_recurso, name='excluirServicoRecurso'),

    # Passo 5 ModeloAssinatura
    path('cadastrarmodeloassinatura', views.cadastrar_modelo_assinatura, name='cadastrarModeloAssinatura'),
    path('listarmodeloassinatura/', views.listar_modelo_assinatura, name='listarModeloAssinatura'),
    path('editarmodeloassinatura/<int:pk>/', views.editar_modelo_assinatura, name='editarModeloAssinatura'),
    path('excluirmodeloassinatura/<int:pk>/', views.excluir_modelo_assinatura, name='excluirModeloAssinatura'),

    path('getvalorunitario/', views.get_valor_unitario, name='getValorunitario'),
    path('getservicos/', views.get_servicos, name='getServicos'),    
    path('getmetodospagamento/', views.get_metodos_pagamento, name='getMetodosPagamento'),        

    path('getdashboard/', views.get_dashboard, name='getDashboard'),
    # outras URLs...
    
]

    