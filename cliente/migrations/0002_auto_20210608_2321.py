# Generated by Django 3.2 on 2021-06-09 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(default='N tem email ainda', max_length=30),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereço',
            field=models.CharField(default='N tem endereço ainda', max_length=70),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone1',
            field=models.CharField(default='N tem telefone ainda', max_length=11),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone2',
            field=models.CharField(default='N tem telefone ainda', max_length=11),
        ),
    ]