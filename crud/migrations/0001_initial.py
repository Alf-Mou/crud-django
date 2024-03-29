# Generated by Django 5.0.3 on 2024-03-16 23:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=16, unique=True)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('idade', models.IntegerField()),
                ('cpf', models.CharField(max_length=11)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crud.usuario')),
            ],
        ),
    ]
