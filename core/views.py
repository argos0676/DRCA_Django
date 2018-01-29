# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from core.models import Aluno, Disciplina, Secretaria
from django.views.generic import ListView
from easy_pdf.views import PDFTemplateView

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def sobre(request):
    template = loader.get_template('sobre.html')
    return HttpResponse(template.render({}, request))

def alunoInfo(request,aluno_id):
	al = Aluno.objects.get(id=aluno_id)
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

def secretariaAdmin(request, id):
    from django.core.urlresolvers import reverse  
    from django.utils.six.moves.urllib.parse import quote

    obj =  al = Secretaria.objects.get(id=2)
    opts = obj._meta
    obj_url = reverse(
        'admin:%s_%s_change' % (opts.app_label, opts.model_name),
        args=(id,),
        current_app='core',
    )
    return HttpResponseRedirect(obj_url)

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

def some_view(request,aluno_id):
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    response = HttpResponse(content_type='application/pdf')
    al = Aluno.objects.get(id=aluno_id)
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
    import xlsxwriter
    from datetime import datetime
    from io import BytesIO
    output = BytesIO()
    # Feed a buffer to workbook
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet("Alunos") #add nova planilha
    alunos = Aluno.objects.all()
    bold = workbook.add_format({'bold': True}) #negrito
    columns = ["Id", "Matricula","Nome", "Data de Nascimento", "Sexo", "Curso"]
    
    row = 0
    for i,elem in enumerate(columns):
        worksheet.write(row, i, elem, bold)
    row += 1
    col = 0

    date_format = workbook.add_format({'num_format': 'd mmmm yyyy'})

    # Now fill other rows with columns
    for a in alunos:
        date = datetime.strptime(a.nascimento.__str__(), "%Y-%m-%d")
        worksheet.write_number(row, col, a.id)
        worksheet.write_number(row, col+1, a.matricula)
        worksheet.write_string(row, col+2, a.nome)
        worksheet.write_datetime(row, col+3, date, date_format)
        worksheet.write_string(row, col+4, a.sexo)
        worksheet.write_string(row, col+5, a.curso.nome)
        row += 1
        
    # Close workbook for building file
    workbook.close()
    output.seek(0)
    response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return response

def contato(request): 
    from core.forms import ContactForm
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            sender = form.cleaned_data.get("sender")
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")

            if subject and message and sender:
                # from django.core.mail import send_mail, BadHeaderError
                # try:
                #     send_mail(subject, message, sender, ['leonardoalmeida.al@gmail.com'], fail_silently=False)
                # except BadHeaderError:
                #     return HttpResponse('Invalid header found.')
                # return HttpResponseRedirect('/')
                from django.core import mail
                connection = mail.get_connection()

                # Manually open the connection
                connection.open()

                # Construct an email message that uses the connection
                email1 = mail.EmailMessage(
                    subject,
                    message,
                    sender,
                    ['leonardoalmeida.al@gmail.com'],
                    connection=connection,
                )
                email1.send()
                connection.close()
            else:
                return HttpResponse('Make sure all fields are entered and valid.')

    return render(request, 'contato.html', {'form': form})