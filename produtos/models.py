from django.db import models
from django.urls import reverse

# Create your models here.

class Produto(models.Model):
    UNIT = (
        ('m', 'm'),
        ('mm', 'mm'),
        ('L', 'L'),
        ('un', 'un')
    )
    codigo=models.CharField(max_length=8,primary_key=True)
    nome=models.CharField(max_length=30)
    tipo=models.CharField(max_length=10)
    qntd=models.IntegerField(default=0)
    unit=models.CharField(max_length=3, choices=UNIT)
    preco_compra=models.FloatField(default=0)
    preco_venda=models.FloatField(default=0)
    nome_fornecedor=models.ForeignKey('fornecedor.Fornecedor', blank=True, null=True,on_delete=models.CASCADE)

    def get_edit_url(self):
        return reverse('produtos:edit', args=[self.pk])
    def get_delete_url(self):
        return reverse('produtos:delete', args=[self.pk])
    def __str__(self):
        return self.nome

    def nome_exibir(self):
        return self.nome + " -  (" + self.codigo + ")"

