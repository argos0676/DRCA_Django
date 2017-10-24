# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from core.models import Aluno
from datetime import datetime

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def alunos(request):
    alunos = Aluno.objects.all()
    template = loader.get_template('alunos.html')
    context = RequestContext(request,{'alunos':alunos})
    return HttpResponse(template.render(context))

def alunoInfo(request,user_id):
	al = Aluno.objects.get(id=user_id)
	template = loader.get_template('alunoInfo.html')
	context = RequestContext(request,{'al':al})
	return HttpResponse(template.render(context))