# Generated by Django 3.2.7 on 2021-10-26 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='alunos',
            field=models.ManyToManyField(related_name='zones', to='perfis.Alunos'),
        ),
    ]