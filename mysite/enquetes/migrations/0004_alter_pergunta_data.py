# Generated by Django 4.0.4 on 2022-05-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0003_alter_pergunta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='data',
            field=models.DateTimeField(verbose_name='Data de publicação'),
        ),
    ]
