from django.db import models
# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome')
    aniversario = models.DateField(help_text='Aniversário')
    email = models.EmailField(help_text='e-mail')
    fone = models.CharField(max_length=11, help_text='Telefone')
    def __str__(self):
        return self.nome
