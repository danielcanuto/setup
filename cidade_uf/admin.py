from django.contrib import admin

from cidade_uf.models import Capitais, Cidades, UnidadeFederativa, CidadeUF, Regiao
# Register your models here.
admin.site.register(Cidades)
admin.site.register(Capitais)
admin.site.register(UnidadeFederativa)
admin.site.register(CidadeUF)
admin.site.register(Regiao)