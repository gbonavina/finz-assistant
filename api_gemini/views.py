from django.http import JsonResponse
from .main import insights, melhorAtivo, comparativo
from django.contrib.auth.decorators import login_required
from core.models import Ativo
import requests

@login_required
def get_insights(request):
    ativos = Ativo.objects.filter(usuario=request.user)
    
    dados = {}
    for ativo in ativos:
        dados[ativo.codigo] = {
            "Quantidade (cotas)": ativo.quant,
            "Preço que comprei": ativo.price,
            "Cotação": ativo.cotacao,
            "Dividend Yield": ativo.dividend_yield,
            "P/VP": ativo.p_vp,
            "Liquidez Diária": ativo.liquidez_diaria,
            "Variação (12M)": ativo.variacao_12m,
            "P/L": ativo.p_l,
        }
    
    result = insights(dados)
    return JsonResponse({'result': result})

@login_required
def get_investimento(request):
    ativos = Ativo.objects.filter(usuario=request.user)
    
    dados = {}
    for ativo in ativos:
        dados[ativo.codigo] = {
            "Quantidade (cotas)": ativo.quant,
            "Preço que comprei": ativo.price,
            "Cotação": ativo.cotacao,
            "Dividend Yield": ativo.dividend_yield,
            "P/VP": ativo.p_vp,
            "Liquidez Diária": ativo.liquidez_diaria,
            "Variação (12M)": ativo.variacao_12m,
            "P/L": ativo.p_l,
        }
    
    result = melhorAtivo(dados)
    return JsonResponse({'result': result})


@login_required
def get_comparativo(request):
    ativos = Ativo.objects.filter(usuario=request.user)
    ibovespa = requests.get(f'http://127.0.0.1:8000/indices/IBOV')
    dados = {}
    for ativo in ativos:
        dados[ativo.codigo] = {
            "Quantidade (cotas)": ativo.quant,
            "Preço que comprei": ativo.price,
            "Cotação": ativo.cotacao,
            "Dividend Yield": ativo.dividend_yield,
            "P/VP": ativo.p_vp,
            "Liquidez Diária": ativo.liquidez_diaria,
            "Variação (12M)": ativo.variacao_12m,
            "P/L": ativo.p_l,
            "Ibovespa" : ibovespa
        }
    
    result = comparativo(dados)
    return JsonResponse({'result': result})
