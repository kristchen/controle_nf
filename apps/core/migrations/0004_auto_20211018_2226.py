# Generated by Django 3.2.8 on 2021-10-18 22:26

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211016_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='comercial_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='legal_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cnpj',
            field=localflavor.br.models.BRCNPJField(max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
