from django.db import models

# Create your models here.
class Account(models.Model):
    codigo=models.CharField(max_length=8,primary_key=True)
    