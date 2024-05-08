from django.urls import path
from projetos import views

app_name = 'projetos'

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('<int:projeto_id>/detail/', views.projeto_single, name='single_projeto'),
    
    #CRUD
    path('create/', views.create, name='projeto_forms'),
    path('update/<int:projeto_id>/', views.update, name='update'),
    path('delete/<int:projeto_id>/', views.delete, name='delete'),
]