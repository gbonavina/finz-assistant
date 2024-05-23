from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import aiohttp
import asyncio

async def scrape_acoes(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    card_body = soup.find_all(class_='_card-body', limit=5)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        data[keys[i]] = text

    return data

async def scrape_bdrs(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    card_body = soup.find_all(class_='_card-body', limit=5)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        data[keys[i]] = text

    return data

async def scrape_cripto(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    card_body = soup.find_all(class_='_card-body', limit=5)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        data[keys[i]] = text

    return data

async def scrape_etfs(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

        soup = BeautifulSoup(page_source, 'html.parser')
        card_body = soup.find_all(class_='_card-body', limit=5)

        data = {}

        for i, box in enumerate(card_body):
            text = box.get_text().strip()
            text = text.replace('\n', '')
            data[keys[i]] = text

        return data
    
async def scrape_etfs_i(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

        soup = BeautifulSoup(page_source, 'html.parser')
        card_body = soup.find_all(class_='_card-body', limit=5)

        data = {}

        for i, box in enumerate(card_body):
            text = box.get_text().strip()
            if keys[i] == "Cotação":
                values = text.split("\n")
                formatted_value = ""
                for val in values:
                    if val.strip():  
                        formatted_value += val.strip() + " "
                data[keys[i]] = formatted_value.strip()
            elif keys[i] == 'Variação (12M)':  
                text = text.replace('\n', ' ')  
                data[keys[i]] = text  
            else:
                data[keys[i]] = text



        return data

async def scrape_fiis(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    card_body = soup.find_all(class_='_card-body', limit=5)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        data[keys[i]] = text

    return data


async def scrape_stocks(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    card_body = soup.find_all(class_='_card-body', limit=5)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        if keys[i] == "Cotação":
            values = text.split("\n")
            formatted_value = ""
            for val in values:
                if val.strip():  
                    formatted_value += val.strip() + " "
            data[keys[i]] = formatted_value.strip()
        else:
            data[keys[i]] = text

    return data

async def scrape_reits(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    card_body = soup.find_all(class_='_card-body', limit=5)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        if keys[i] == "Cotação":
            values = text.split("\n")
            formatted_value = ""
            for val in values:
                if val.strip():  
                    formatted_value += val.strip() + " "
            data[keys[i]] = formatted_value.strip()
        else:
            data[keys[i]] = text


    return data


async def scrape_moedas(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    if keys == ['Cotação', 'Variação (24h)', 'Variação (12M)']:
        card_body = soup.find_all(class_='_card-body', limit=3)
    else:
        card_body = soup.find_all(class_='_card-body', limit=4)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        data[keys[i]] = text

    return data

async def scrape_indices(url, keys):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            
            page_source = await response.text()

    soup = BeautifulSoup(page_source, 'html.parser')
    card_body = soup.find_all(class_='_card-body', limit=5)

    data = {}

    for i, box in enumerate(card_body):
        text = box.get_text().strip()
        data[keys[i]] = text

    return data