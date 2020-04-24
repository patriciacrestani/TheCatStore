from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, F, FloatField
from .models import Carrinho
from .forms import AtualizaProdutoForm
from produto.models import Produto

@login_required
def ver_carrinho(request):
    carrinho = Carrinho.objects.filter(user=request.user)
    resultado = carrinho.aggregate(
        total=Sum(F('preco') * F('quantidade'), output_field=FloatField()))

    if resultado['total']:
        total = '{0:.2f}'.format(resultado['total'])
    else:
        total = '0,00'

    lista_de_ids = []
    lista_de_forms =[]
    lista_de_sub = []
    for item in carrinho:
        lista_de_ids.append(item.produto.id)
        lista_de_forms.append(AtualizaProdutoForm(initial={'quantidade': item.quantidade}))
        lista_de_sub.append(item.quantidade * item.preco)

    return render(request, 'carrinho/carrinho.html', {'listas': zip(carrinho, lista_de_forms, lista_de_sub),
                                                      'total': total,
                                                      'lista_de_ids': lista_de_ids})

@login_required
def adiciona_ao_carrinho(request):
    if request.POST:
        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)

        linha_carrinho = Carrinho.objects.filter(user=request.user, produto=produto).first()
        if linha_carrinho:
            linha_carrinho.quantidade += 1
            linha_carrinho.save()
        else:
            Carrinho.objects.create(produto=produto, user=request.user, preco=produto.preco, quantidade=1)

    return redirect(ver_carrinho)


@login_required
def remove_do_carrinho(request):
    produto_id = request.POST.get('produto_id')
    produto = get_object_or_404(Produto, id=produto_id)
    linha_carrinho = Carrinho.objects.filter(user=request.user, produto=produto).first()
    linha_carrinho.delete()

    carrinho = Carrinho.objects.filter(user=request.user)
    resultado = carrinho.aggregate(
        total=Sum(F('preco') * F('quantidade'), output_field=FloatField()))

    if resultado['total']:
        total = '{0:.2f}'.format(resultado['total'])
    else:
        total = '0,00'

    return render(request, 'carrinho/carrinho.html', {'carrinho': carrinho,
                                                      'total': total})
@login_required
def atualiza_produto(request):
    carrinho = get_object_or_404(Carrinho, produto_id=request.POST.get('produto_id'), user=request.user)
    form = AtualizaProdutoForm(request.POST, instance=carrinho)
    if form.is_valid:
        form.save()
        resultado = Carrinho.objects.filter(user=request.user).aggregate(
            total=Sum(F('quantidade') * F('preco'), output_field=FloatField()))

        if resultado['total']:
            total = '{0:.2f}'.format(resultado['total'])
        else:
            total = '0,00'
        c2 = get_object_or_404(Carrinho, produto_id=request.POST.get('produto_id'), user=request.user)
        subtotal = c2.quantidade * c2.preco
        print(subtotal)
        return render(request, 'carrinho/carrinho.html', {'carrinho': carrinho,
                                                          'total': total,
                                                          'subtotal': subtotal})

    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar alterar um produto.')