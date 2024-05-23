# Finz-API <img src="finz.png" alt="Ícone" width="35" height="35">

A Finz-API é uma API criada para fornecer informações atuais sobre diversos tipos de ativos financeiros (Nacionais e Internacionais). Através dela, os usuários podem obter uma variedade de dados como por exemplo:
- Cotação
- Variação
- P/L (Preço/Lucro)
- P/VP (Preço/Valor Patrimonial)
- Dividend Yield

## Como usar

### Requisitos
- Python 3.x instalado no seu sistema
- Bibliotecas necessárias (instaladas via pip): `requests`, `BeautifulSoup4`

### Passo a passo
1. Clone o repositório da Finz-API para o seu ambiente local:
```bash
git clone https://github.com/marcoshollmann/finz-api
```
2. Acesse o diretório da API:
```bash
cd finz-api
```
3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

Use os métodos disponíveis para obter informações sobre os ativos financeiros desejados. Cada método corresponde a um tipo de ativo:

- Ações: `get_acoes(nome_ativo)`
- FIIs (Fundos de Investimento Imobiliário): `get_fiis(nome_ativo)`
- BDRs (Brazilian Depositary Receipts): `get_bdrs(nome_ativo)`
- Criptomoedas: `get_criptomoedas(nome_ativo)`
- ETFs (Exchange-Traded Funds): `get_etfs(nome_ativo)`
- ETFs Internacionais: `get_etfs_internacionais(nome_ativo)`
- Stocks (Ações internacionais): `get_stocks(nome_ativo)`
- REITs (Real Estate Investment Trusts): `get_reits(nome_ativo)`
- Moedas: `get_moedas(nome_ativo)`

Substitua `nome_ativo` pelo nome do ativo desejado.

### Exemplo de uso

```python
from finz import app
from fastapi.testclient import TestClient

client = TestClient(app)

lista_acoes = [
    "PETR4", "VALE3", "ITUB4", "BBDC4", "ABEV3", "BBAS3", "SUZB3", "MGLU3", "GGBR4", "CIEL3",
    "B3SA3", "CMIG4", "ELET3", "UGPA3", "WEGE3", "LAME4", "BRKM5", "JBSS3", "EMBR3", "MRVE3",
    "RADL3", "FLRY3", "IRBR3", "HAPV3", "QUAL3", "CYRE3", "ENBR3", "UGPA3", "RENT3", "BIDI4",
    "CSNA3", "CPFE3", "EGIE3", "GOAU4", "MULT3", "SULA11", "TAEE11", "BBDC3", "CVCB3", 'TECN3',
    "HYPE3", "BTOW3", "SBSP3", "BRML3", "GOLL4", "CMIG3", "CCRO3", "SMLS3", "ECOR3",'POSI3', 
]

for i in lista_acoes:
    response_acao = client.get(f"/acoes/{i}")
    info_acao = response_acao.json()
    print(info_acao)
```
- Em ambiente de testes este exemplo de 50 ativos obteve um tempo de execução inferior a 1 minuto (≅ 1 segundo por ativo).

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Créditos

Este projeto foi desenvolvido por [Marcos Hollmann](https://www.linkedin.com/in/marcos-hollmann-401812204/) e [Gabriel Bonavina](https://www.linkedin.com/in/gabriel-leal-bonavina-8388a7267/).
