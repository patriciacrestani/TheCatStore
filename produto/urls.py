from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('produto/<int:id>/<slug:slug_produto>', views.produto, name='produto'),
    path('gato/<int:id>/<slug:slug_gato>', views.gato, name='gato'),
    path('todos-produtos', views.todos_produtos, name='todosprodutos'),
    path('todos-gatos/', views.todos_gatos, name='todosgatos'),
    path('todos-gatos/<int:id>/<slug:slug_raca>', views.gatos_filtrados, name='gatosfiltrados'),
    path('todos-produtos/<int:id>/<slug:slug_categoria>', views.produtos_filtrados, name='produtosfiltrados'),
    path('adicionar-gato', views.criar_gato, name='criargato'),
    path('adicionar-produto', views.criar_produto, name='criarproduto'),
    path('pesquisa-produtos/', views.lista_produto, name='pesquisa-produtos'),
    path('administrar-gatos/', views.administrar_gatos, name='adm-gatos'),
    path('administrar-produtos/', views.administrar_produtos, name='adm-produtos'),
    path('edita-produto/<int:id>/', views.edita_produto, name='editaproduto'),
    path('edita-gato/<int:id>/', views.edita_gato, name='editagato'),
    path('remove-produto/<int:id>', views.remove_produto, name='removeproduto'),
    path('remove-gato/<int:id>', views.remove_gato, name='removegato'),
]