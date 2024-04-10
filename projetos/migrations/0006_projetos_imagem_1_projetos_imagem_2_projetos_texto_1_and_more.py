# Generated by Django 5.0.3 on 2024-04-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0005_alter_projetos_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='imagem_1',
            field=models.ImageField(blank=True, upload_to='picture/%Y/%m'),
        ),
        migrations.AddField(
            model_name='projetos',
            name='imagem_2',
            field=models.ImageField(blank=True, upload_to='picture/%Y/%m'),
        ),
        migrations.AddField(
            model_name='projetos',
            name='texto_1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projetos',
            name='texto_2',
            field=models.TextField(blank=True),
        ),
    ]