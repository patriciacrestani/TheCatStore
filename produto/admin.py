from django.contrib import admin

# Register your models here.

from produto.models import Gato, Produto, Categoria
admin.site.register(Gato)
admin.site.register(Produto)
admin.site.register(Categoria)