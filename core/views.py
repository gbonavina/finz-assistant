from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ativo
import requests
import logging
from datetime import date

logger = logging.getLogger(__name__)

@login_required(login_url='/auth/login')
def ativos(request):
    ativos = Ativo.objects.filter(usuario=request.user)
    for ativo in ativos:
        if isinstance(ativo.quant, float):
            ativo.quant = format(ativo.quant, ".2f").rstrip('0').rstrip('.')
        if isinstance(ativo.cotacao, float):
            ativo.cotacao = format(ativo.cotacao, ".2f")
        if isinstance(ativo.price, float):
            ativo.price = format(ativo.price, ".2f")

    saldo_total = sum([float(ativo.price) * float(ativo.quant) for ativo in ativos])
    return render(request, "index.html", {"ativos": ativos, "saldo_total": saldo_total})

def erro(request):
    return render(request, 'erro.html')

def erro_ativo(request):
    return render(request, 'erro_ativo.html')
    
@login_required(login_url='/auth/login')
def salvar(request):
    if request.method == 'POST':
        codigo = request.POST.get("codigo")
        quant = request.POST.get("quant")
        price = request.POST.get("price")
        tipo = request.POST.get("tipo")

        try:
            quant = float(quant)
        except ValueError:
            quant = -1

        try:
            price = float(price)
        except ValueError:
            price = -1

        if tipo is None:
            tipo = ''

        if codigo is None:
            codigo = ''

        ativo = Ativo.objects.create(
            usuario=request.user, codigo=codigo, quant=quant, price=price, tipo=tipo
        )

        if tipo == '':
            ativo.delete()
            ativos = Ativo.objects.filter(usuario=request.user)
            return render(request, 'erro.html', {'ativos': ativos})

        if codigo == '':
            ativo.delete()
            ativos = Ativo.objects.filter(usuario=request.user)
            return render(request, 'erro.html', {'ativos': ativos})
        
        if price < 0 or quant < 0:
            ativo.delete()
            ativos = Ativo.objects.filter(usuario=request.user)  
            return render(request, 'erro_ativo.html', {'ativos': ativos})
        
        
        try:
            response = requests.get(f'http://127.0.0.1:8000/{ativo.tipo}/{ativo.codigo}')
            if response.status_code == 200:
                data = response.json()
                logger.debug(f"Received data: {data}")

                today = date.today()
                date_key = today.strftime("%d/%m/%Y")

                if date_key in data and ativo.codigo in data[date_key]:
                    data_ativo = data[date_key][ativo.codigo]

                    ativo.cotacao = data_ativo.get('Cotação', 0.0) 
                    ativo.dividend_yield = data_ativo.get('Dividend Yield', '-')
                    ativo.p_vp = data_ativo.get('P/VP', '-')
                    ativo.liquidez_diaria = data_ativo.get('Liquidez Diária', '-')
                    ativo.p_l = data_ativo.get('P/L', '-')
                    ativo.variacao_24h = data_ativo.get('Variação (24h)', '-')
                    ativo.variacao_12m = data_ativo.get('Variação (12M)', '-')
                    ativo.variacao_24m = data_ativo.get('Variação (24M)', '-')
                    ativo.variacao_60m = data_ativo.get('Variação (60M)', '-')

                else:
                    logger.warning(f"Expected data for date '{date_key}' and code '{ativo.codigo}' not found in response.")
            else:
                logger.error(f"Failed to fetch data: {response.status_code}")
            
            ativo.save()
            return redirect('ativos')
        except AttributeError:
            ativo.delete()
            ativos = Ativo.objects.filter(usuario=request.user)
            return render(request, 'erro.html', {'ativos': ativos})
    else:
        return redirect('ativos')

@login_required(login_url='/auth/login')
def editar(request, id):
    ativo = get_object_or_404(Ativo, id=id, usuario=request.user)
    ativo.quant = str(ativo.quant).replace(',', '.')
    ativo.price = str(ativo.price).replace(',', '.')
    return render(request, "update.html", {"ativo": ativo})

@login_required(login_url='/auth/login')
def update(request, id):
    if request.method == 'POST':
        ativo = get_object_or_404(Ativo, id=id, usuario=request.user)
        codigo = request.POST.get("codigo")
        quant = request.POST.get("quant")
        price = request.POST.get("price")

        if price is not None:
            price = float(price)

        if codigo:  
            ativo.codigo = codigo
        ativo.quant = quant
        if price is not None:
            ativo.price = price

        ativo.save()
        return redirect('ativos')
    else:
        return redirect('editar', id=id)

@login_required(login_url='/auth/login')
def delete(request, id):
    ativo = get_object_or_404(Ativo, id=id, usuario=request.user)
    ativo.delete()
    return redirect('ativos')

@login_required(login_url='/auth/login')
def plataforma(request):
    usuario = request.user
    ativos = Ativo.objects.filter(usuario=usuario)
    for ativo in ativos:
        if isinstance(ativo.quant, float):
            ativo.quant = format(ativo.quant, ".2f").rstrip('0').rstrip('.').replace('.', ',')
        if isinstance(ativo.cotacao, float):
            ativo.cotacao = format(ativo.cotacao, ".2f").replace('.', ',')
        if isinstance(ativo.price, float):
            ativo.price = format(ativo.price, ".2f").replace('.', ',')

    saldo_total = sum([float(ativo.price.replace(',', '.')) * float(ativo.quant.replace(',', '.')) for ativo in ativos])
    return render(request, 'plataforma.html', {'ativos': ativos, 'saldo_total': saldo_total})
