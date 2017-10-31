# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from core.models import Aluno, Disciplina, Secretaria
from django.views.generic import ListView

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

def secretariaAdmin(request):   
    from django.core.urlresolvers import reverse 
    return HttpResponseRedirect(reverse('admin:app_list', kwargs={'app_label':'core'}))

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
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    
    response = HttpResponse(content_type='application/pdf')
    al = Aluno.objects.get(id=user_id)
    filename = str(al)
    response['Content-Disposition'] = 'attachment; filename={0}.pdf'.format(filename)
    
    pdf = canvas.Canvas(response)
    pdf.setFont('Courier',12)

    tupla = ('Dados do Aluno para impressão:', 'Nome: '+str(al),'Matrícula: '+str(al.matricula), 'Curso: '+str(al.curso.nome))
    lista = pdf.beginText(inch * 1, inch * 10)
    for i in range(0,len(tupla)):
        lista.textLine(tupla[i])

    pdf.drawText(lista)
    #pdf.drawString(30, 750,conteudo)
    pdf.showPage()
    pdf.save()

    return response
