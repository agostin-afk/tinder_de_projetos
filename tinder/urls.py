
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('projetos.urls')),
    path('', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]
