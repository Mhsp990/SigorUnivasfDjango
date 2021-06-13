from django.db import models

# Create your models here.
class Funcionario(models.Model):
    cpf=models.CharField(max_length=11,primary_key=True)
    nome=models.CharField(max_length=30)
    telefone1=models.CharField(max_length=11)
    telefone2=models.CharField(max_length=11,blank=True,null=True)
    endereço=models.CharField(max_length=70,blank=True,null=True)
    email=models.CharField(max_length=40)
    data_nascimento=models.DateField('aniversário')
    cargo=models.CharField(max_length=15)

    def __str__(self):
        return self.nome
