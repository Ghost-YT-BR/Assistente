from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.home, name="home"),
    path("emergencial/", views.emergencial, name="emergencial"),
    path("tipo/", views.tipo_ocorrencia, name="tipo_ocorrencia"),
    path("questionario/<str:tipo_nome>/", views.questionario, name="questionario"),
    path("resumo/", views.resumo, name="resumo"),
    
    # Nova rota de procedimentos
    path("procedimentos/<int:ocorrencia_id>/", views.procedimentos, name="procedimentos"),
]
