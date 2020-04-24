from django import forms
from django.core.validators import RegexValidator
from .models import Carrinho

class RemoveProdutoForm(forms.Form):
    class Meta:
        fields = ('produto_id',)

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=True)

class CompraProdutoForm(forms.Form):
    class Meta:
        fields = ('produto_id',)

    produto_id = forms.CharField(widget=forms.HiddenInput(), required=True)

class AtualizaProdutoForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = ('quantidade',)

    quantidade = forms.CharField(
        error_messages={'required': 'Campo obrigatório.', },
        validators=[RegexValidator(regex='^[0-9]{1,5}$', message="Informe o valor no formato 99999.")],
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm quantidade',
                                      'maxlength': '5',
                                      'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'}),
        required=True)