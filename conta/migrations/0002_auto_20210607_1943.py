# Generated by Django 2.2.5 on 2021-06-07 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conta', '0001_initial'),
        ('cliente', '0001_initial'),
        ('ordemServico', '0001_initial'),
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='OS',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ordemServico.OrdemDeServico'),
        ),
        migrations.AddField(
            model_name='conta',
            name='conta_cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente'),
        ),
        migrations.AddField(
            model_name='conta',
            name='conta_fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fornecedor.Fornecedor'),
        ),
    ]