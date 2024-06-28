"""
Repositório para gerenciar a busca de dados de FIIs do site Funds Explorer.
"""

import requests
import bs4

class FIIDataRepository:
    # fetch_fii_data(fii_code): Busca os dados do FII especificado do site Funds Explorer.
    def fetch_fii_data(self, fii_code):
        url = f'https://www.fundsexplorer.com.br/funds/{fii_code}'
        response = requests.get(url)
        
        if response.status_code != 200:
            return None, f"Erro ao acessar o site: {response.status_code}"
        
        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        try:
            indicators_boxes = soup.find_all("div", class_="indicators__box")
            data = {}

            for box in indicators_boxes:
                title = box.find("p").get_text(strip=True)
                value_element = box.find("b")
                data[title] = value_element.get_text(strip=True)

            if not data:
                return None, "Erro ao encontrar os dados na página."
        except AttributeError:
            return None, "Erro ao encontrar os dados na página. Verifique a estrutura HTML."

        return data, None
