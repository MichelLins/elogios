from django.db import models
from django.utils import timezone

class Elogio(models.Model):
    autor = models.CharField(max_length=100)
    destinatario = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Elogio de {self.autor} para {self.destinatario}"
