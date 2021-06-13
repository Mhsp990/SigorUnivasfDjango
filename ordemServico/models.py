from django.db import models


# Create your models here.
class OrdemDeServico(models.Model):
    STATUS = (
        ('Aberto', 'Aberto'),
        ('Em andamento', 'Em andamento'),
        ('Feito', 'Feito'),
    )
    numeroOS =  models.AutoField(primary_key=True)
    data_created = models.DateTimeField(auto_now_add= True, null= True)
    valor = models.FloatField(null=True, blank=True, default=None)
    cliente = models.ForeignKey('cliente.Cliente', null=True, on_delete = models.SET_NULL) 
    veiculos = models.ForeignKey('veiculos.Veiculo', null=True, on_delete = models.SET_NULL) 
    status = models.CharField(max_length=50,null=True, choices=STATUS)
    produtos=models.ManyToManyField('produtos.Produto',null=True,blank=True)
    funcionario=models.ForeignKey('funcionario.Funcionario', null=True, on_delete = models.SET_NULL)
    descricao=models.CharField(max_length=250,null=True,blank=True)
    def __str__(self):
        return str(self.numeroOS)
 