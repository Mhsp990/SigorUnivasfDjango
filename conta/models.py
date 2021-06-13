from django.db import models

# Create your models here.
class Conta(models.Model):
    TIPO = (
        ('Dinheiro', 'Dinheiro'),
        ('Cartão', 'Cartão'),
        ('Boleto', 'Boleto')
    )

    STATUS = (
        ('A pagar', 'A pagar'),
        ('A receber', 'A receber')
    )

    cod_Conta=models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=STATUS)
    data_emissao = models.DateTimeField(auto_now_add= True, null= True)
    data_vencimento = models.DateField()
    tipo_pagamento = models.CharField(max_length=10, choices=TIPO)
    descricao = models.TextField(blank=True)
    

    conta_cliente=models.ForeignKey('cliente.Cliente', null=True,blank=True, on_delete=models.CASCADE)
    conta_fornecedor=models.ForeignKey('fornecedor.Fornecedor', blank=True, null=True,on_delete=models.CASCADE)
    OS = models.ForeignKey('ordemServico.OrdemDeServico',null=True,on_delete=models.SET_NULL)
    

    def __str__(self):
        return ("Conta -"+ str(self.cod_Conta))