# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_str, smart_unicode

class Credito(models.Model):
    d_credito = models.IntegerField()
    d_credito_p = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()
    
    def __unicode__(self):
        return smart_unicode(self.d_credito)
    
class Departamento(models.Model):
    nome = models.CharField(max_length=30)
    
    def __unicode__(self):
        return smart_unicode(self.nome)
    
class Professor(models.Model):
    nome = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, null=True)
    
    def __unicode__(self):
        return smart_unicode(self.nome)
        
class Secretaria(models.Model):
    nome = models.CharField(max_length=30)
    tipo = models.IntegerField()
    departamento = models.ForeignKey(Departamento, null=True)
    
    def __unicode__(self):
        return smart_unicode(self.nome)
       
class Curso(models.Model):
    nome = models.CharField(max_length=30)
    secretaria = models.ForeignKey(Secretaria, null=True)
    
    def __unicode__(self):
        return smart_unicode(self.nome)
        
class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    obg_let = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    credito = models.ForeignKey(Credito)
    d_requisito = models.ManyToManyField('Disciplina',blank=True)
    curso = models.ForeignKey(Curso)
    professor = models.ForeignKey(Professor,null=True)
    
    def __unicode__(self):
        return smart_unicode(self.nome)
    
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    matricula = models.IntegerField()
    curso = models.ForeignKey(Curso)
    credito = models.ForeignKey(Credito)
    disciplinas = models.ManyToManyField(Disciplina,blank=True)
    
    def __unicode__(self):
        return smart_unicode(self.nome)