from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions

from api.views import CNABView, TransacaoView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Challenge Api",
      terms_of_service="https://policies.google.com/terms",
      contact=openapi.Contact(email="mrcsz.m@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('cnab/', CNABView.as_view()),
    path('transacao/', TransacaoView.as_view())
]
