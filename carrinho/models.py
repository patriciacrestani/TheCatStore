from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from produto.models import Produto
from django.conf import settings


class Carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    quantidade = models.IntegerField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    def get_absolute_path(self):
        return reverse('carrinho', args=[self.id])

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.title
