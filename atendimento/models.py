from django.db import models
 
class Ocorrencia(models.Model):
    TIPO_CHOICES = [
        ("EM", "Emergencial"),
        ("NE", "Não Emergencial"),
    ]
 
    # Dados Iniciais
    nome_solicitante = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    estado = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    referencia = models.TextField(blank=True, null=True)
    
    # Classificação
    tipo_atendimento = models.CharField(max_length=2, choices=TIPO_CHOICES, default="EM")
    tipo_ocorrencia = models.CharField(max_length=100, blank=True, null=True) # Ex: Incêndio, Explosão
    
    # Questionário
    respostas_questionario = models.JSONField(blank=True, null=True) # Salva as perguntas e respostas
    
    data_criacao = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"{self.nome_solicitante} - {self.tipo_ocorrencia}"
 