# Generated by Django 3.2.7 on 2021-09-14 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=255)),
                ('cargo_atual', models.CharField(max_length=255)),
                ('empresa_atual', models.CharField(max_length=255)),
                ('rede_social', models.CharField(max_length=255)),
                ('lattes', models.CharField(max_length=255)),
                ('interesses', models.CharField(max_length=255)),
                ('relato_pessoal', models.CharField(max_length=255)),
                ('contatos', models.ManyToManyField(related_name='_perfis_alunos_contatos_+', to='perfis.Alunos')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nivel', models.CharField(max_length=255)),
                ('campus', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255)),
                ('data_formatura', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=255)),
                ('alunos', models.ManyToManyField(to='perfis.Alunos')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfis.curso')),
            ],
        ),
    ]
