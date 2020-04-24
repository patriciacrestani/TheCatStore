from produto.forms import PesquisaProdutoForm
from produto.models import Categoria

def base_needs(request):
    categoria = Categoria.objects.all()
    form = PesquisaProdutoForm()
    return {'categorias' : categoria,
            'form': form}