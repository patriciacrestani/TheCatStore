from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.ver_carrinho, name='carrinho'),
    path('add-carrinho/', views.adiciona_ao_carrinho, name='add-carrinho'),
    path('remove-carrinho/', views.remove_do_carrinho, name='remove-carrinho'),
    path('atualiza-produto/', views.atualiza_produto, name='atualiza-produto')
]