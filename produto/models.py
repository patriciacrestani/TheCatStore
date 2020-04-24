from django.db import models
from django.urls import reverse
from django.conf import settings


class Categoria(models.Model):
    nome = models.CharField(max_length=50, default='', null=False, blank=False)
    slug = models.SlugField(unique=True)

    def get_absolute_path(self):
        return reverse('produtosfiltrados', args=[self.id, self.slug])

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class Raca(models.Model):
    nome = models.CharField(max_length=50, default='', null=False, blank=False)
    slug = models.SlugField(unique=True)

    def get_absolute_path(self):
        return reverse('gatosfiltrados', args=[self.id, self.slug])

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(default='', max_length=200, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default='')
    descricao = models.CharField(default='', max_length=600, null=False, blank=False)
    preco = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, null=False, blank=False)
    likes = models.IntegerField(default=1, null=False, blank=False)
    dislikes = models.IntegerField(default=1, null=False, blank=False)
    quantidade = models.IntegerField(default=1, null=False, blank=False)
    marca = models.CharField(default='', max_length=150, null=False, blank=False)
    fabricante = models.CharField(default='', max_length=150, null=False, blank=False)
    dimensoes = models.CharField(default='', max_length=100, null=False, blank=False)
    peso = models.DecimalField(default=0.0, max_digits=3, decimal_places=1, null=False, blank=False)
    garantia = models.IntegerField(default=0, null=False, blank=False)
    cor = models.CharField(default='', max_length=100, null=False, blank=False)
    material = models.CharField(default='', max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='produtos')
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='produtos',
                             on_delete=models.DO_NOTHING,
                             null=True)

    def get_absolute_path(self):
        return reverse('produto', args=[self.id, self.slug])

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.title

class Gato(models.Model):
    nome = models.CharField(default='', max_length=200, null=False, blank=False)
    descricao = models.CharField(default='', max_length=600, null=False, blank=False)
    preco = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, null=False, blank=False)
    idade = models.IntegerField(default=1, null=False, blank=False)
    tamanho = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, null=False, blank=False)
    peso = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, null=False, blank=False)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING, default='')
    localizacao = models.CharField(default='', max_length=200, null=False, blank=False)
    castrado = models.BooleanField(default=False, null=False, blank=True)
    filhos = models.BooleanField(default=False, null=False, blank=True)
    irmaos = models.BooleanField(default=False, null=False, blank=True)
    fiv = models.BooleanField(default=False, null=False, blank=True)
    felv = models.BooleanField(default=False, null=False, blank=True)
    doencas = models.CharField(default='', max_length=200, null=False, blank=True)
    vacinado = models.BooleanField(default=False, null=False, blank=True)
    raiva = models.BooleanField(default=False, null=False, blank=True)
    vermifugado = models.BooleanField(default=False, null=False, blank=True)
    imagem = models.ImageField(upload_to='gatos')
    slug = models.SlugField(unique=True)

    def get_absolute_path(self):
        return reverse('gato', args=[self.id, self.slug])

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.title

