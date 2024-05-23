from fastapi import FastAPI
from core.finz_api.api.functions import scrape_acoes, scrape_fiis, scrape_bdrs, scrape_cripto, scrape_etfs, scrape_etfs_i, scrape_stocks, scrape_reits, scrape_moedas, scrape_indices
from datetime import date

app = FastAPI()
today = date.today()
hoje = today.strftime("%d/%m/%Y")

tags_metadata = [
    {"name": "FIIs", "description": "Operações relacionadas a Fundos de Investimento Imobiliário (FIIs)"},
    {"name": "Ações", "description": "Operações relacionadas a ações"},
    {"name": "BDRs", "description": "Operações relacionadas a Brazilian Depositary Receipts (BDRs)"},
    {"name": "ETFs", "description": "Operações relacionadas a Exchange-Traded Funds (ETFs)"},
    {"name": "Criptomoedas", "description": "Operações relacionadas a criptomoedas"},
    {"name": "Stocks", "description": "Operações relacionadas a ações internacionais"},
    {"name": "Reits", "description": "Operações relacionadas a Real Estate Investment Trusts (REITs)"},
]

@app.get("/", tags=['Home'])
async def root():
    return {"message": "Bem vindo a Finz-API"}

@app.get("/fiis/{codigo}", tags=["FIIs"], summary="Obter informações sobre Fundos de Investimento Imobiliário (FIIs)")
async def get_fii(codigo: str):
    """Obtém informações sobre um Fundo de Investimento Imobiliário (FII) específico."""
    url = f'https://investidor10.com.br/fiis/{codigo}'
    keys = ['Cotação', 'Dividend Yield', 'P/VP', 'Liquidez Diária', 'Variação (12M)']
    data = await scrape_fiis(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/acoes/{codigo}", tags=["Ações"], summary="Obter informações sobre Ações")
async def get_acoes(codigo: str):
    """Obtém informações sobre uma Ação específica."""
    url = f'https://investidor10.com.br/acoes/{codigo}'
    keys = ['Cotação', 'Variação (12M)','P/L', 'P/VP', 'Dividend Yield']
    data = await scrape_acoes(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/bdrs/{codigo}", tags=["BDRs"], summary="Obter informações sobre BDRs")
async def get_bdrs(codigo: str):
    """Obtém informações sobre um Brazilian Depositary Receipt (BDR) específico."""
    url = f'https://investidor10.com.br/bdrs/{codigo}'
    keys = ['Cotação', 'Variação (12M)','P/L', 'P/VP', 'Dividend Yield']
    data = await scrape_bdrs(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/etfs/{codigo}", tags=["ETFs"], summary="Obter informações sobre ETFs")
async def get_etfs(codigo: str):
    """Obtém informações sobre um Exchange-Traded Fund (ETF) nacional específico."""
    url = f'https://investidor10.com.br/etfs/{codigo}'
    keys = ['Cotação', 'Variação (12M)','P/L', 'P/VP', 'Dividend Yield']
    data = await scrape_etfs(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/etfs-internacional/{codigo}", tags=["ETFs"], summary="Obter informações sobre ETFs internacionais")
async def get_etfs_internacional(codigo: str):
    """Obtém informações sobre um Exchange-Traded Fund (ETF) internacional específico."""
    url = f'https://investidor10.com.br/etfs-global/{codigo}'
    keys = ['Cotação', 'Variação (12M)','P/L', 'P/VP', 'Dividend Yield']
    data = await scrape_etfs_i(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/criptomoedas/{codigo}", tags=["Criptomoedas"], summary="Obter informações sobre Criptomoedas")
async def get_criptomoedas(codigo: str):
    """Obtém informações sobre uma Criptomoeda específica."""
    url = f'https://investidor10.com.br/criptomoedas/{codigo}'
    keys = [f'{codigo.capitalize()} hoje', 'Valor em R$','Capitalização', 'Variação (24h)', 'Variação (12M)']
    data = await scrape_cripto(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/stocks/{codigo}", tags=["Stocks"], summary="Obter informações sobre Ações Internacionais")
async def get_stocks(codigo: str):
    """Obtém informações sobre uma Ação Internacional específica."""
    url = f'https://investidor10.com.br/stocks/{codigo}'
    keys = ['Cotação', 'Variação (12M)','P/L', 'P/VP', 'Dividend Yield']
    data = await scrape_stocks(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/reits/{codigo}", tags=["Reits"], summary="Obter informações sobre Real Estate Investment Trusts (REITs)")
async def get_reits(codigo: str):
    """Obtém informações sobre um REITs específico."""
    url = f'https://investidor10.com.br/reits/{codigo}'
    keys = ['Cotação', 'Variação (12M)','P/L', 'P/VP', 'Dividend Yield']
    data = await scrape_reits(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/moedas/{codigo}", tags=["Moedas"], summary="Obter informações sobre Moedas")
async def get_reits(codigo: str):
    """Obtém informações sobre uma Moeda específica."""
    url = f'https://investidor10.com.br/moedas/{codigo}'
    if codigo.upper() == 'USD':
        keys = ['Cotação', 'Variação (24h)', 'Variação (12M)']
    else:
        keys = [f'{codigo.capitalize()} hoje','Cotação em dólares', 'Variação (24h)', 'Variação (12M)']
    data = await scrape_moedas(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}

@app.get("/indices/{codigo}", tags=["Índices"], summary="Obter informações sobre alguns índices")
async def get_indices(codigo: str):
    """Obtém informações sobre os índices IBOVESPA e S&P 500."""
    url = f"https://investidor10.com.br/indices/{codigo}"
    keys = ['Valor Atual', 'Variação (12M)', 'Variação (60M)']
    data = await scrape_indices(url, keys)
    return {hoje:{f"{codigo.upper()}": data}}