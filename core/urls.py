# from django.contrib import admin
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()

from django.urls import include, path, re_path
from fusion.views import FileUploadAPIView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from fusion import views
from fusion.views import FileUploadAPIView

app_name = "api"

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("api/", include(router.urls)),
    # path("test", views.TestView.as_view(), name="test"),
    # re_path(r"^upload/(?P<filename>[^/]+)$", FileUploadView.as_view()),
    # path("test", views.test, name="test"),
    path("upload-file/", FileUploadAPIView.as_view(), name="upload-file"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
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
