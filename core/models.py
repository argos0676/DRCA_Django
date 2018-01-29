# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
import datetime

class Credito(models.Model):
    d_credito = models.IntegerField()
    d_credito_p = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()
    
    def __str__(self):
        return str(self.d_credito)
    
class Departamento(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.nome
        
class Secretaria(models.Model):
    nome = models.CharField(max_length=30)
    tipo = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.nome
       
class Curso(models.Model):
    nome = models.CharField(max_length=30)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.nome
        
class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    obg_let = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    ##d_requisito = models.ManyToManyField(Disciplina)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    
    SEXO_CHOICES = (
        (u'masculino',u'Masculino'),
        (u'feminino',u'Feminino'),
        )

    nome = models.CharField(max_length=30)
    matricula = models.IntegerField()
    nascimento = models.DateField(default=datetime.date.today)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null = True)
    sexo = models.CharField(max_length = 50, choices = SEXO_CHOICES)
    credito = models.ForeignKey(Credito,on_delete=models.CASCADE, null = True)
    disciplinas = models.ManyToManyField(Disciplina)
    
    def __str__(self):
        return self.nome

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(self.id,))