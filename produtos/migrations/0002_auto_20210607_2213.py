# Generated by Django 2.2.5 on 2021-06-08 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='unit',
            field=models.CharField(choices=[('m', 'm'), ('mm', 'mm'), ('L', 'L'), ('un', 'un')], max_length=3),
        ),
    ]