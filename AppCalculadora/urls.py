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

    # Módulo Servico
    path('listarservico/', views.listar_servico, name='listarServico'),
    path('cadastrarservico/', views.cadastrar_servico, name='cadastrarServico'),
    path('editarservico/<int:pk>/', views.editar_servico, name='editarServico'),
    path('excluirservico/<int:pk>/', views.excluir_servico, name='excluirServico'),    

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

]


