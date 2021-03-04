from django.contrib import admin
from django.urls import path, re_path, include

from sici_site.views import home
from sici_site.views import home_SIDOM
from sici_site.views import siconi
from sici_site.views import unidade
from sici_site.views import geral
from sici_site.views import MDcontratos
from sici_site.views import MDcontratos_individual
from sici_site.views import MDcontratos_total
from sici_site.views import contrato_analitico
from sici_site.views import edita_contrato

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^unidade/(?P<cod_ua>\d+)/$', unidade),
    path('accounts/', include('django.contrib.auth.urls')),
    path('geral/', geral),
    path('home_SIDOM/', home_SIDOM),
    path('siconi/', siconi),
    path('admin/', admin.site.urls),
    path('contratos/<int:contrato>/', contrato_analitico, name='contrato_analitico'),
    path('edita_contrato/<int:id>/', edita_contrato, name='edita_contrato'),
    path('MDcontratos/', MDcontratos),
    path('MDcontratos_total/', MDcontratos_total),
    path('MDcontratos_individual/', MDcontratos_individual, name='MDcontratos_individual'),
]