from django.db import models
from django.contrib.admin import widgets
# Create your models here.


class Servico(models.Model):
    nome = models.CharField(max_length=100, help_text='Serviço')
    tempo = models.DurationField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome
