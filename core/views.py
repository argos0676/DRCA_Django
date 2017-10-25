# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from core.models import Aluno, Disciplina

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def alunos(request):
    alunos = Aluno.objects.all()
    template = loader.get_template('alunos.html')
    return HttpResponse(template.render({'alunos':alunos},request))

def alunoInfo(request,user_id):
	al = Aluno.objects.get(id=user_id)
	template = loader.get_template('alunoInfo.html')
	return HttpResponse(template.render({'al':al},request))

def disciplinas(request):
	disciplinas = Disciplina.objects.all()
	template = loader.get_template('disciplinas.html')
	return HttpResponse(template.render({'disciplinas':disciplinas},request))