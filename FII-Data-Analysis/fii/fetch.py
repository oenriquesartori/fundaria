"""
Módulo responsável por buscar e extrair dados de FIIs do site Funds Explorer.

Funções:
- get_fii_data(fii_code): Busca os dados do FII especificado e os retorna em formato de dicionário.
"""

import requests
import bs4

def get_fii_data(fii_code):
    url = f'https://www.fundsexplorer.com.br/funds/{fii_code}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return None, f"Erro ao acessar o site: {response.status_code}"
    
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    try:
        # Buscar os dados utilizando seletores CSS mais precisos
        indicators_boxes = soup.find_all("div", class_="indicators__box")

        # Inicializar um dicionário para armazenar os dados
        data = {}

        # Iterar sobre os elementos encontrados e extrair os valores corretos
        for box in indicators_boxes:
            title = box.find("p").get_text(strip=True)
            value_element = box.find("b")
            data[title] = value_element.get_text(strip=True)

        # Verificar se algum dado essencial não foi encontrado
        if not data:
            return None, "Erro ao encontrar os dados na página."

    except AttributeError:
        return None, "Erro ao encontrar os dados na página. Verifique a estrutura HTML."

    return data, None
