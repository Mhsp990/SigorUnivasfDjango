# Generated by Django 3.2 on 2021-06-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20210608_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone1',
            field=models.CharField(default='N tem ', max_length=11),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone2',
            field=models.CharField(blank=True, default='N tem ', max_length=11, null=True),
        ),
    ]
