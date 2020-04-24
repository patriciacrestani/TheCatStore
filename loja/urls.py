"""loja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from produto.urls import urlpatterns as urlproduto
from autenticacao.urls import urlpatterns as urlautenticacao
from carrinho.urls import urlpatterns as urlcarrinho

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('quemsomos', views.quemsomos, name='quemsomos'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('', include(urlproduto)),
    path('', include(urlautenticacao)),
    path('', include(urlcarrinho)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
