from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path('user/login/', views.login, name='login'),
    path('user/create/', views.register, name='register'),
    path('user/logout/', views.logout, name='logout'),
    path('user/update/', views.update_user, name='user_update'),
    
]