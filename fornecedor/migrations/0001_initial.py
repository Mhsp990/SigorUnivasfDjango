# Generated by Django 2.2.5 on 2021-06-07 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('codigo', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
    ]
