from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from fusion.views import *
from fusion.views import ExcelImportAPIView
from usuario.router import router as usuario_router

app_name = "api"

router = DefaultRouter()
urlpatterns = [
    path("api/excel-import/", ExcelImportAPIView.as_view(), name="excel-import"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

# Adicionando configuração de rotas de mídia se DEBUG for True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
