# Generated by Django 5.0.3 on 2024-03-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0003_alter_categoria_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='numero',
            field=models.CharField(default='45', max_length=50),
        ),
    ]
