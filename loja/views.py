from django.core.paginator import Paginator
from django.shortcuts import render
from produto.models import Gato, Produto
from django.db.models import Q

def home_page(request):
    lista_gatos = Gato.objects.all()
    gatos1 = lista_gatos[:4]
    gatos2 = lista_gatos[4:8]

    lista_racao_areia = Produto.objects.filter(Q(categoria=1) | Q(categoria=2) | Q(categoria=3))
    racao_areia1 = lista_racao_areia[:4]
    racao_areia2 = lista_racao_areia[4:8]

    lista_brinquedos_arranhadores = Produto.objects.filter(Q(categoria=4) | Q(categoria=8))
    brinquedos_arranhadores1 = lista_brinquedos_arranhadores[:4]
    brinquedos_arranhadores2 = lista_brinquedos_arranhadores[4:8]

    lista_outros = Produto.objects.filter(Q(categoria=5) | Q(categoria=6) | Q(categoria=7) | Q(categoria=9))
    outros1 = lista_outros[:4]
    outros2 = lista_outros[4:8]

    return render(request, 'loja/index.html', {'gatos1': gatos1,
                                               'gatos2': gatos2,
                                               'racaoareia1': racao_areia1,
                                               'racaoareia2': racao_areia2,
                                               'brinquedos1': brinquedos_arranhadores1,
                                               'brinquedos2': brinquedos_arranhadores2,
                                               'outros1': outros1,
                                               'outros2': outros2})

def quemsomos(request):
    return render(request, 'loja/quemsomos.html')

def cadastro(request):
    return render(request, 'loja/cadastro.html')

