from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do esquema da API
schema_view = get_schema_view(
    openapi.Info(
        title="Pastebin API",
        default_version='v1',
        description="Documentação da API",
        # termos de uso, contato, etc. (opcional)
    ),
    public=True,  # Permite acesso público à documentação
)

# Se você estiver usando routers, pode manter:
# router = routers.DefaultRouter()
# router.register(...)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rota para a documentação Swagger UI
    re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # Rota para o esquema JSON (opcional)
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api-auth/', include('rest_framework.urls')),
]

# Se houver arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)