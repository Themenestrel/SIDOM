from datetime import datetime, timedelta
from .forms import MdContratosDiarioForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import make_aware
from django.http import HttpResponse

from sici_site.models import Dados
from sici_site.models import MdContratosDiario

def home(request):

    if request.method == 'GET':

        dados = MdContratosDiario.objects.all().order_by('-data_diario')

        return render(request, 'sici_site/home.html', {'dados': dados})

def home_SIDOM(request):

    if request.method == 'GET':

        dados = MdContratosDiario.objects.all().order_by('-data_diario')

        return render(request, 'sici_site/home_SIDOM.html', {'dados': dados})


def siconi(request):
    if request.method == 'GET':
        tipo_consulta = request.GET.get("consulta", None)
        busca = request.GET.get("busca")

        if tipo_consulta == "cd_ua":
            dados = Dados.objects.filter(cd_ua=busca)
            if dados is not None:
                return redirect(f'unidade/{busca}')
        elif tipo_consulta == "nome":
            dados = Dados.objects.filter(nome_ua__icontains=busca).order_by('nome_ua').values('cd_ua',
                                                                                              'nome_ua',
                                                                                              'titular').distinct()
        elif tipo_consulta == "titular":
            dados = Dados.objects.filter(titular__icontains=busca).order_by('titular').values('cd_ua',
                                                                                              'nome_ua',
                                                                                              'titular').distinct()
        else:
            dados = None

        return render(request, 'sici_site/siconi.html', {'dados': dados, 'tipo': tipo_consulta})


def unidade(request, **kwargs):
    if request.method == 'GET':
        if 'data' in request.GET:
            data = request.GET['data'].split('-')
            data_busca = make_aware(datetime(int(data[0]), int(data[1]), int(data[2])) + timedelta(1))
        else:
            hoje = datetime.now()
            data_busca = make_aware(datetime(hoje.year, hoje.month, hoje.day) + timedelta(1))

        busca = kwargs['cod_ua']
        dados = Dados.objects.filter(cd_ua=busca, data_criacao_registro__lt=data_busca).order_by(
            'data_criacao_registro').last()
        fim = Dados.objects.filter(cd_ua=busca, data_criacao_registro__gte=data_busca).order_by(
            'data_criacao_registro').first()
        if fim is not None:
            fim = fim.data_criacao_registro

        return render(request, 'sici_site/unidade.html', {'dados': dados, 'fim': fim})


def geral(request):
    dados = Dados.objects.all().order_by('nome_ua').values('cd_ua', 'nome_ua', 'titular').distinct()

    return render(request, 'sici_site/geral.html', {'dados': dados})


def contratos(request):
    dados = MdContratosDiario.objects.all()

    return render(request, 'sici_site/contratos.html', {'dados': dados})


def contrato_analitico(request, contrato):

    dados = MdContratosDiario.objects.filter(ug_contrato=contrato).order_by('-data_diario')

    dados_sici = Dados.objects.filter(cd_ua=contrato).order_by('-data_criacao_registro')

    return render(request, 'sici_site/contrato_analitico.html', {'dados': dados, 'dados_sici': dados_sici})


def edita_contrato(request, id):

    dados = MdContratosDiario.objects.filter(id=id).values().last()

    if request.method == 'POST':
        print('1')
        item = get_object_or_404(MdContratosDiario, id=id)
        form = MdContratosDiarioForm(request.POST, instance=item)
        print(form)
        if form.is_valid():
            print('3')
            form.save()
            return redirect('/home_SIDOM/')
    else:
        print('2')
        item = MdContratosDiario.objects.filter(id=id).values().last()
        form = MdContratosDiarioForm(initial=item)
        print(form)

    return render(request, 'sici_site/edita_contrato.html', {'form': form, 'item': item, 'dados': dados})

def MDcontratos(request):
    if request.method == 'GET':
        if 'data_diario' in request.GET:
            data = request.GET['data_diario'].split('-')
            data_busca = make_aware(datetime(int(data[0]), int(data[1]), int(data[2])) + timedelta(1))
        else:
            hoje = datetime.now()
            data_busca = make_aware(datetime(hoje.year, hoje.month, hoje.day) + timedelta(1))

        dados = MdContratosDiario.objects.filter(data_diario=data_busca).order_by('data_diario').last()

        #        dados = MdContratosDiario.objects.all().order_by('-data_diario')

        return render(request, 'sici_site/MDcontratos.html', {'dados': dados})


def MDcontratos_individual(request):

    dados = MdContratosDiario.objects.all().order_by('-data_diario')

    return render(request, 'sici_site/MDcontratos_individual.html', {'dados': dados})


def MDcontratos_total(request):

    dados = MdContratosDiario.objects.all().order_by('-data_diario').values('data_diario').distinct()

    return render(request, 'sici_site/MDcontratos_total.html', {'dados': dados})
