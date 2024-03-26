from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categoria(models.Model):
    name = models.CharField(max_length=50)
    class Meta():
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self) -> str:
        return self.name

class Projetos(models.Model):
    nome = models.CharField(max_length=255, blank=False)
    sigla = models.CharField(max_length=10, blank=True)
    numero = models.CharField(max_length=50, blank=False)
    email_responsavel = models.EmailField(max_length=254, blank=False)
    data_cadastro = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    logo = models.ImageField(blank=True,upload_to='picture/%Y/%m')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta():
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
    def __str__(self) -> str:
        if self.sigla:
            return self.sigla
        return self.nome