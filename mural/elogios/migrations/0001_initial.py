# Generated by Django 5.1 on 2024-08-12 23:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elogio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('destinatario', models.CharField(max_length=100)),
                ('mensagem', models.TextField()),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
