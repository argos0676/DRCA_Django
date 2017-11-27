# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from core.models import *
admin.site.site_title = 'DRCA'
admin.site.site_header = 'Administração - DRCA'
admin.site.index_title = 'Ambiente de administração do site'

class AlunoAdmin(admin.ModelAdmin):
    model = Aluno
    list_display = ['nome','matricula','curso']
    list_filter = ['nome']
    search_fields = ['nome','matricula']
    save_on_top = True

class CreditoAdmin(admin.ModelAdmin):
    model = Credito
    list_display = ['d_credito','d_credito_p','a_credito_o','a_credito_l']
    list_filter = ['d_credito']
    save_on_top = True

class DisciplinaAdmin(admin.ModelAdmin):
    model = Disciplina
    list_display = ['nome','codigo','obg_let','status']
    list_filter = ['nome']
    search_fields = ['nome','codigo']
    save_on_top = True

class SecretariaAdmin(admin.ModelAdmin):
    model = Secretaria
    list_display = ['nome','tipo']
    list_filter = ['nome','tipo']
    search_fields = ['nome','tipo']
    save_on_top = True

class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']
    save_on_top = True

class CursoAdmin(admin.ModelAdmin):
    model = Curso
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']
    save_on_top = True

class Departamentodmin(admin.ModelAdmin):
    model = Departamento
    list_display = ['nome']
    list_filter = ['nome']
    search_fields = ['nome']
    save_on_top = True

admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Credito,CreditoAdmin)
admin.site.register(Disciplina,DisciplinaAdmin)
admin.site.register(Secretaria,SecretariaAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Departamento,Departamentodmin)