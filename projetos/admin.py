from django.contrib import admin
from projetos import models

@admin.register(models.Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = 'id','nome','sigla', 'show',
    list_filter = 'data_cadastro',
    ordering = ()
    search_fields = 'id', 'nome', 'sigla',
    list_editable = 'show',
    list_per_page = 20
    list_max_show_all = 500
    list_display_links = 'nome','sigla',
    
    
@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',