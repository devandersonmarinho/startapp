from django.db import models
from apps.clientes.models import Cliente
from apps.servicos.models import Servico
from apps.Funcionarios.models import Funcionario


# Create your models here.
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    servicos = models.ManyToManyField(Servico)
    profissinal = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    agendamento = models.DateTimeField(auto_now=False, auto_now_add=False)