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

def analyze_fii(data):
    analysis = {}

    # Funções auxiliares
    def check_liquidity(value):
        if value > 1000000:
            return 'Bom'
        elif 500000 <= value <= 1000000:
            return 'Razoável'
        else:
            return 'Ruim'

    def check_dividend_yield(dy):
        dy_float = float(dy.replace(',', '.').strip('%'))
        if dy_float >= 8:
            return 'Bom'
        elif 5 <= dy_float < 8:
            return 'Razoável'
        else:
            return 'Ruim'

    def check_pvp(pvp):
        pvp_float = float(pvp.replace(',', '.'))
        if pvp_float < 1:
            return 'Bom'
        elif 1 <= pvp_float <= 1.5:
            return 'Razoável'
        else:
            return 'Ruim'

    def check_monthly_return(return_value):
        return_float = float(return_value.replace(',', '.').strip('%'))
        if return_float >= 0:
            return 'Bom'
        else:
            return 'Ruim'

    # Liquidez Média Diária
    try:
        liquidez_media_diaria = float(data.get("Liquidez Média Diária", "").replace('.', '').replace(',', '.').replace('K', '000').replace('M', '000000').replace('B', '000000000').strip())
        analysis['Liquidez Média Diária'] = check_liquidity(liquidez_media_diaria)
    except ValueError:
        analysis['Liquidez Média Diária'] = 'Desconhecido'

    # Dividend Yield
    try:
        dividend_yield = data.get("Dividend Yield", "")
        analysis['Dividend Yield'] = check_dividend_yield(dividend_yield)
    except ValueError:
        analysis['Dividend Yield'] = 'Desconhecido'

    # Patrimônio Líquido
    try:
        patrimonio_liquido = float(data.get("Patrimônio Líquido", "").replace('.', '').replace(',', '.').replace('K', '000').replace('M', '000000').replace('B', '000000000').strip())
        if patrimonio_liquido >= 3000000000: 
            analysis['Patrimônio Líquido'] = 'Bom'
        else:
            analysis['Patrimônio Líquido'] = 'Razoável'
    except ValueError:
        analysis['Patrimônio Líquido'] = 'Desconhecido'

    # Valor Patrimonial (P/VP)
    try:
        pvp = float(data.get("P/VP", "").replace(',', '.'))
        if pvp < 1:
            analysis['P/VP'] = 'Bom'
        elif 1 <= pvp <= 1.5:
            analysis['P/VP'] = 'Razoável'
        else:
            analysis['P/VP'] = 'Ruim'
    except ValueError:
        analysis['P/VP'] = 'Desconhecido'

    # Análise do Risco com base nos critérios combinados
    if (analysis.get('Liquidez Média Diária', '') == 'Bom' and
        analysis.get('Dividend Yield', '') == 'Bom' and
        analysis.get('Patrimônio Líquido', '') == 'Bom' and
        analysis.get('P/VP', '') == 'Bom'):
        risk = 'Seguro'
    elif (analysis.get('Liquidez Média Diária', '') in ['Razoável', 'Bom'] and
          analysis.get('Dividend Yield', '') in ['Razoável', 'Bom'] and
          analysis.get('P/VP', '') == 'Razoável'):
        risk = 'Neutro'
    else:
        risk = 'Arriscado'

    analysis['Risco'] = risk

    return analysis

def main():
    while True:
        fii_code = input("Digite o código do FII (ou 'Finalizar' para sair): ").strip().lower()
        
        if fii_code == 'finalizar':
            print("Encerrando o programa...")
            break
        
        data, error = get_fii_data(fii_code)
        
        if error:
            print(error)
            continue

        print(f"Dados do FII {fii_code.upper()}:")
        for key, value in data.items():
            print(f"{key}: {value}")
        
        analysis = analyze_fii(data)
        print("\nAnálise do FII:")
        for key, value in analysis.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()

#testado v1