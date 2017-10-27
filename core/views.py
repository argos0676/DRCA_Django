# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from core.models import Aluno, Disciplina, Secretaria
from django.views.generic import ListView
from reportlab.pdfgen import canvas

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def alunoInfo(request,user_id):
	al = Aluno.objects.get(id=user_id)
	template = loader.get_template('alunoInfo.html')
	return HttpResponse(template.render({'al':al},request))

class ListaSecretarias(ListView):
    template_name = 'secretarias.html'
    model = Secretaria
    context_object_name = 'secretarias'
	# paginate_by = 100
 
    def get_queryset(self, **kwargs):
        secretarias = Secretaria.objects.all()
        result = self.request.GET.get('pesquisar_por')
 
        # Buscar por disciplinas
        if result is not None:
            secretarias = secretarias.filter(nome__icontains=result)
        return secretarias

class ListaDisciplinas(ListView):
    template_name = 'disciplinas.html'
    model = Disciplina
    context_object_name = 'disciplinas'
	# paginate_by = 100
 
    def get_queryset(self, **kwargs):
        disciplinas = Disciplina.objects.all()
        result = self.request.GET.get('pesquisar_por')
 
        # Buscar por disciplinas
        if result is not None:
            disciplinas = disciplinas.filter(nome__icontains=result)
        return disciplinas

class ListaAlunos(ListView):
    template_name = 'alunos.html'
    model = Aluno
    context_object_name = 'alunos'
	# paginate_by = 100
 
    def get_queryset(self, **kwargs):
        alunos = Aluno.objects.all()
        result = self.request.GET.get('pesquisar_por')
 
        # Buscar por aluno
        if result is not None:
            alunos = alunos.filter(nome__icontains=result)
        return alunos

def some_view(request,user_id):
    # usar pip install reportlab
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Aluno.pdf"'

    al = Aluno.objects.get(id=user_id)

 # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 750,str(al))

 # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    return response