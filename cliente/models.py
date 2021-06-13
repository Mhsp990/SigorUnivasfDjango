from django.db import models

# Create your models here.
class Cliente(models.Model):
    cpf = models.CharField(max_length=11,primary_key=True)
    nome=models.CharField(max_length=30)
    telefone1=models.CharField(max_length=11,default='N tem ')
    telefone2=models.CharField(max_length=11,default='N tem ',null=True,blank=True)
    endereço=models.CharField(max_length=70,default='N tem endereço ainda')
    email=models.CharField(max_length=30, default='N tem email ainda')
    
    def __str__(self):
        return self.nome
