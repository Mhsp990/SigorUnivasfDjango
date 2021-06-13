from django.db import models
from django.urls import reverse

# Create your models here.
class Fornecedor(models.Model):
    codigo=models.CharField(max_length=15,primary_key=True)
    nome=models.CharField(max_length=30,default='N tem nome ainda')
    telefone1=models.CharField(max_length=11,default='N tem telefone ainda')
    telefone2=models.CharField(max_length=11,default='N tem telefone ainda',null=True,blank=True)
    endereço=models.CharField(max_length=70,default='N tem endereco ainda')
    email=models.CharField(max_length=30,default='N tem email ainda')
    produtos=models.ManyToManyField('produtos.Produto',blank=True,null=True)

    def __str__(self):
        return self.codigo

    def get_edit_url(self):
        return reverse('fornecedor:edit', args=[self.pk])
    def get_delete_url(self):
        return reverse('fornecedor:delete', args=[self.pk])