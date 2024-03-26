from django.contrib import admin
from projetos import models

@admin.register(models.Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    ...
    
    
@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...