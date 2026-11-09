from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")), # Adiciona esta linha
    path("", include("atendimento.urls")),
]