from django.db import models

# Create your models here.
class Veiculo(models.Model):
    placa=models.CharField(max_length=7,primary_key=True)
    marca=models.CharField(max_length=15)
    modelo=models.CharField(max_length=15)
    cor=models.CharField(max_length=10)
    cliente = models.ForeignKey('cliente.Cliente', null=True,blank=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.placa

    def nome_exibir(self):
        return self.modelo + " -  (" + self.placa + ")"