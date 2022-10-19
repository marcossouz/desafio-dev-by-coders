from django.db import models


class Transacao(models.Model):
    tipo = models.SmallIntegerField()
    descricao = models.CharField(max_length=255, unique=True)
    natureza = models.CharField(max_length=10)
    sinal = models.CharField(max_length=1)

    def __str__(self):
        return self.descricao


class CNAB(models.Model):
    tipo = models.ForeignKey(Transacao, on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)

    def __str__(self):
        return self.nome_loja

    class Meta:
        unique_together = ['tipo', 'data', 'valor', 'cpf', 'cartao', 'hora', 'dono_loja', 'nome_loja']

