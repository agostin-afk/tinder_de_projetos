# Generated by Django 5.0.3 on 2024-03-26 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.AlterModelOptions(
            name='projetos',
            options={'verbose_name': 'Projeto', 'verbose_name_plural': 'Projetos'},
        ),
        migrations.RenameField(
            model_name='projetos',
            old_name='category',
            new_name='categoria',
        ),
    ]
