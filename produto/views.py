from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from produto.forms import PesquisaProdutoForm, ProdutoForm, GatoForm
from carrinho.forms import CompraProdutoForm
from produto.models import Produto, Gato, Categoria, Raca
from django.template.defaultfilters import slugify
from django.contrib import messages


def produto(request, id, slug_produto):
    p = get_object_or_404(Produto, pk=id)
    form_compra_produto = CompraProdutoForm(initial={'produto_id': id})
    return render(request, 'produto/produto.html', {'produto' : p,
                                                    'form_compra_produto': form_compra_produto})

def gato(request, id, slug_gato):
    cat = get_object_or_404(Gato, pk=id)
    return render(request, 'produto/gato.html', {'gato' : cat})

def todos_produtos(request):
    lista_produtos = Produto.objects.all()
    paginator = Paginator(lista_produtos, 5)
    pagina = request.GET.get('pagina')
    produtos = paginator.get_page(pagina)
    return render(request, 'produto/lista-produtos.html', {'produtos' : produtos})

def todos_gatos(request):
    lista_gatos = Gato.objects.all()
    racas = Raca.objects.all()
    paginator = Paginator(lista_gatos, 5)
    pagina = request.GET.get('pagina')
    gatos = paginator.get_page(pagina)
    return render(request, 'produto/lista-gatos.html', {'gatos' : gatos,
                                                        'racas' : racas})

def gatos_filtrados(request, id, slug_raca):
    racas = Raca.objects.all()
    lista_gatos = Gato.objects.filter(raca=id)
    paginator = Paginator(lista_gatos, 5)
    pagina = request.GET.get('pagina')
    gatos = paginator.get_page(pagina)
    return render(request, 'produto/lista-gatos.html', {'gatos' : gatos,
                                                        'racas' : racas})

def produtos_filtrados(request, id, slug_categoria):
    categorias = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(categoria=id)
    paginator = Paginator(lista_produtos, 5)
    pagina = request.GET.get('pagina')
    produtos = paginator.get_page(pagina)
    return render(request, 'produto/lista-produtos.html', {'produtos': produtos,
                                                           'categorias': categorias})
@login_required
def criar_gato(request):
    if request.POST:
        gato_id = request.POST.get('gato_id')
        if gato_id:
            gato = get_object_or_404(Gato, pk=gato_id)
            gato_form = GatoForm(request.POST, request.FILES, instance=gato)
        else:
            gato_form = GatoForm(request.POST, request.FILES)
        if gato_form.is_valid():
            gato = gato_form.save(commit=False)
            if gato_id:
                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
            else:
                gato.slug = slugify(gato.nome)
            gato.save()
            return redirect('gato', id=gato_id, slug_gato=gato.slug)
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        gato_form = GatoForm()
    return render(request, 'administracao/criar-gato.html', {'form': gato_form})

@login_required
def criar_produto(request):
    if request.POST:
        produto_id = request.POST.get('produto_id')
        if produto_id:
            produto = get_object_or_404(Produto, pk=produto_id)
            produto_form = ProdutoForm(request.POST, request.FILES, instance=produto)
        else:
            produto_form = ProdutoForm(request.POST, request.FILES)
        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            if produto_id:
                messages.add_message(request, messages.INFO, 'Produto alterado com sucesso!')
            else:
                produto.slug = slugify(produto.nome)
                produto.user = request.user
                messages.add_message(request, messages.INFO, 'Produto cadastrado com sucesso!')
            produto.save()
            return redirect('produto', id=produto.id, slug_produto=produto.slug)
        else:
            messages.add_message(request, messages.ERROR, 'Corrija o(s) erro(s) abaixo.')
    else:
        produto_form = ProdutoForm()
    return render(request, 'administracao/criar-produto.html', {'form': produto_form})

def lista_produto(request):
   form = PesquisaProdutoForm(request.GET)
   if (form.is_valid()):
      busca_por = form.cleaned_data['busca_por']
      lista_de_produtos = Produto.objects.filter(nome__icontains=busca_por).order_by('nome')
      paginator = Paginator(lista_de_produtos, 5)
      pagina = request.GET.get('pagina')
      produtos = paginator.get_page(pagina)

      return render(request, 'produto/pesquisa-produto.html', {
         'form': form,
         'produtos': produtos,
         'busca_por': busca_por
      })

   else:
      raise ValueError('Ocorreu um erro inesperado ao tentar pesquisar um produto.')

@login_required
def administrar_gatos(request):
    lista_gatos = Gato.objects.all()
    paginator = Paginator(lista_gatos, 10)
    pagina = request.GET.get('pagina')
    gatos = paginator.get_page(pagina)
    return render(request, 'administracao/administrar-gatos.html', {'gatos': gatos})

@login_required
def administrar_produtos(request):
    lista_produtos = Produto.objects.all()
    paginator = Paginator(lista_produtos, 5)
    pagina = request.GET.get('pagina')
    produtos = paginator.get_page(pagina)
    return render(request, 'administracao/administrar-produtos.html', {'produtos': produtos})

@login_required
def edita_gato(request, id):
    gato = get_object_or_404(Gato, pk=id)
    gato_form = GatoForm(instance=gato)
    gato_form.fields['gato_id'].initial = id
    return render(request, 'administracao/criar-gato.html', {'form': gato_form})

@login_required
def edita_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto_form = ProdutoForm(instance=produto)
    produto_form.fields['produto_id'].initial = id
    return render(request, 'administracao/criar-produto.html', {'form': produto_form})

@login_required
def remove_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('adm-produtos')

@login_required
def remove_gato(request, id):
    gato = get_object_or_404(Gato, id=id)
    gato.delete()
    return redirect('adm-gatos')