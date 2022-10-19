from django.contrib import admin
from django.urls import include, path
from api.views import CNABView, TransacaoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cnab/', CNABView.as_view()),
    path('transacao/', TransacaoView.as_view())
]
