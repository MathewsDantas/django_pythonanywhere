# Generated by Django 4.0.4 on 2022-07-29 01:45

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
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('pontuacao', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Simulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('pont_total', models.DecimalField(decimal_places=2, max_digits=2)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_fim', models.DateField(null=True, verbose_name='Data de encerramento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulado.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('correta', models.BooleanField(default=False)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulado.questao')),
            ],
        ),
        migrations.AddField(
            model_name='questao',
            name='simulado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulado.simulado'),
        ),
    ]
