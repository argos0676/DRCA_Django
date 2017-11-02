from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from core.models import Aluno, Disciplina, Secretaria
from django.views.generic import ListView
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.core.urlresolvers import reverse
from easy_pdf.views import PDFTemplateView
import xlsxwriter
from io import BytesIO

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def sobre(request):
    template = loader.get_template('sobre.html')
    return HttpResponse(template.render({}, request))

def contato(request):
    template = loader.get_template('contato.html')
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

class HelloPDFView(PDFTemplateView):
    template_name = 'pdf.html'

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
        pagesize='A4',
        title='Informações adicionais',
        **kwargs
    )

def excel(request):
    output = BytesIO()
    # Feed a buffer to workbook
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet("users")
    users = Aluno.objects.all()
    bold = workbook.add_format({'bold': True})
    columns = ["id", "nome", "matricula", "curso"]
    # Fill first row with columns
    row = 0
    for i,elem in enumerate(columns):
        worksheet.write(row, i, elem, bold)
    row += 1
    # Now fill other rows with columns
    for user in users:
        worksheet.write(row, 0, user.id)
        worksheet.write(row, 1, user.nome)
        worksheet.write(row, 2, user.matricula)
        worksheet.write(row, 3, user.curso.nome)
        row += 1
    # Close workbook for building file
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return response