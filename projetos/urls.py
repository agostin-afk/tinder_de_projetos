from django.urls import path
from projetos import views

app_name = 'projetos'

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('create/', views.create, name='projeto_forms'),
]