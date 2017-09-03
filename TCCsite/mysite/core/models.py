from django.db import models
from .validators import validate_file_extension

# Create your models here.

class Aluno(models.Model):

	id = models.AutoField (primary_key = True)
	nome = models.CharField(max_length=120)
	cpf = models.CharField(max_length=11)
	document = models.FileField(upload_to='documents/',validators=[validate_file_extension], null = True, blank = True)
		
	def __str__(self):
		return self.nome
		

class Tcc(models.Model):
	
	aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=100)
	curso = models.CharField(max_length=100)

	def __str__(self):
		return self.titulo