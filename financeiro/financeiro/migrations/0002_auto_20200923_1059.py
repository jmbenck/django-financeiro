# Generated by Django 3.1.1 on 2020-09-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Entrada'), (2, 'Saida')]),
        ),
    ]