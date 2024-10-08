from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework import routers

route = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls')),
] + debug_toolbar_urls()
