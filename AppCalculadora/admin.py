# Register your models here.
from django.contrib import admin
from .models import TipoRecurso, Recurso, Servico, ServicoRecurso
from .models import  TipoCusto,Custo, ServicoRecurso, FuncaoCusto, ComportamentoCusto
from .models import  Empresa, EmpresaCusto


admin.site.register(TipoCusto)
admin.site.register(FuncaoCusto)
admin.site.register(ComportamentoCusto)
admin.site.register(Custo)

admin.site.register(TipoRecurso)
admin.site.register(Recurso)
admin.site.register(Servico)
admin.site.register(ServicoRecurso)

admin.site.register(Empresa)
admin.site.register(EmpresaCusto)


