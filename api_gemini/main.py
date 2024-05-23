import os
import google.generativeai as genai
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
else:
    print("Erro: Arquivo .env não encontrado. Configure sua chave API.")
    exit(1)

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

instruction = "Você é um assessor financeiro experiente, seu nome é Finz-Assistant, te darei a seguir os dados dos ativos financeiros da minha carteira de investimentos: use ** apenas quando quiser quebrar uma linha "

def insights(dados):
    personalizado = "me dê insights para minha carteira de investimentos, como por exemplo, qual ação está com bons indicativos de compra, comece se aprensetando"

    prompt = f"{instruction}: {dados}, {personalizado}"
    response = model.generate_content(prompt)
    
    generated_text = response.text
     
    return formatar_texto(generated_text)


def melhorAtivo(dados):
    personalizado = "me fale qual foi o ativo que teve a maior valorização nos ultimos 12 meses e fale sobre os indicativos dele, comece se aprensetando"
    prompt = f"{instruction}: {dados}, {personalizado}"

    response = model.generate_content(prompt)
    generated_text = response.text
    
    return formatar_texto(generated_text)

def comparativo(dados):
    personalizado = "me fale como minha carteira se desempenhou em comparação ao desempenho medio do (IBOVESPA) e fale sobre os indicativos de ambos, comece se aprensetando"
    prompt = f"{instruction}: {dados}, {personalizado}"

    response = model.generate_content(prompt)
    generated_text = response.text
    
    return formatar_texto(generated_text)



def formatar_texto(texto):
    texto = texto.replace("**", "<br>")
    return texto.strip()    