from django import forms
from django.core.validators import RegexValidator
from decimal import Decimal
from .models import Produto, Gato, Raca, Categoria

class PesquisaProdutoForm(forms.Form):
   class Meta:
      fields = ('busca_por')

   busca_por = forms.CharField(
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=False)

class ProdutoForm(forms.ModelForm):
   class Meta:
      model = Produto
      fields = ('produto_id', 'nome', 'categoria', 'descricao', 'preco', 'quantidade', 'marca',
                'fabricante', 'dimensoes', 'peso', 'garantia', 'cor', 'material', 'imagem')

   produto_id = forms.CharField(widget=forms.HiddenInput(), required=False)

   nome = forms.CharField(
      error_messages={'required': 'Campo obrigatório.', 'unique': 'Produto duplicado.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=True)

   categoria = forms.ModelChoiceField(
      error_messages={'required': 'Campo obrigatório.', },
      queryset=Categoria.objects.all().order_by('nome'),
      empty_label='--- Selecione uma categoria ---',
      widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
      required=True)

   descricao = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   preco = forms.DecimalField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True
   )

   quantidade = forms.IntegerField(
      error_messages={'required': 'Campo obrigatório.', },
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   marca = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
      required=True)

   fabricante = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
      required=True)

   dimensoes = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
      required=True)

   peso = forms.IntegerField(
      error_messages={'required': 'Campo obrigatório.', },
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   garantia = forms.IntegerField(
      error_messages={'required': 'Campo obrigatório.', },
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   cor = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
      required=True)

   material = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '200'}),
      required=True)

   imagem = forms.ImageField(
      error_messages={'required': 'Campo obrigatório.'},
      required=True)

class GatoForm(forms.ModelForm):
   class Meta:
      model = Gato
      fields = ('gato_id', 'nome', 'descricao', 'preco', 'idade', 'tamanho', 'peso', 'raca',
                'localizacao', 'castrado', 'filhos', 'irmaos', 'fiv', 'felv', 'doencas', 'vacinado', 'raiva',
                'vermifugado', 'imagem')

   gato_id = forms.CharField(widget=forms.HiddenInput(), required=False)

   nome = forms.CharField(
      error_messages={'required': 'Campo obrigatório.', 'unique': 'Produto duplicado.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '120'}),
      required=True)

   descricao = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   preco = forms.DecimalField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   idade = forms.IntegerField(
      error_messages={'required': 'Campo obrigatório.', },
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '2'}),
      required=True)

   tamanho = forms.DecimalField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   peso = forms.DecimalField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   raca = forms.ModelChoiceField(
      error_messages={'required': 'Campo obrigatório.', },
      queryset=Raca.objects.all().order_by('nome'),
      empty_label='--- Selecione uma categoria ---',
      widget=forms.Select(attrs={'class': 'form-control form-control-sm'}),
      required=True)

   localizacao = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   castrado = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   filhos = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   irmaos = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   fiv = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   felv = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   doencas = forms.CharField(
      error_messages={'required': 'Campo obrigatório.'},
      widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '500'}),
      required=True)

   vacinado = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   raiva = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   vermifugado = forms.BooleanField(
      widget=forms.CheckboxInput(attrs={'class': 'form-control form-control-sm'}))

   imagem = forms.ImageField(
      error_messages={'required': 'Campo obrigatório.'},
      required=True)