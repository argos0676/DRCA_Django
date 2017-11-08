# -*- coding: utf-8 -*-
from django.db import models
import datetime

class Credito(models.Model):
    d_credito = models.IntegerField()
    d_credito_p = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()
    
    def __str__(self):
        return self.d_credito
    
class Departamento(models.Model):
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, null=True)
    
    def __str__(self):
        return self.nome
        
class Secretaria(models.Model):
    nome = models.CharField(max_length=30)
    tipo = models.IntegerField()
    departamento = models.ForeignKey(Departamento, null=True)
    
    def __str__(self):
        return self.nome
       
class Curso(models.Model):
    nome = models.CharField(max_length=30)
    secretaria = models.ForeignKey(Secretaria, null=True)
    
    def __str__(self):
        return self.nome
        
class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    obg_let = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    credito = models.ForeignKey(Credito)
    d_requisito = models.ManyToManyField('Disciplina',blank=True)
    curso = models.ForeignKey(Curso)
    professor = models.ForeignKey(Professor,null=True)
    
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
    curso = models.ForeignKey(Curso)
    sexo = models.CharField(max_length = 50, choices = SEXO_CHOICES)
    credito = models.ForeignKey(Credito,on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina,blank=True)
    
    def __str__(self):
        return self.nome