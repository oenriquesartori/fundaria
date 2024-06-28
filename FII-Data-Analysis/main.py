"""
Arquivo principal do projeto. Gerencia a entrada do usuário e executa a busca e análise dos FIIs.

Funções:
- main(): Função principal que controla o fluxo do programa.
"""

from fii.fetch import get_fii_data
from fii.analyze import analyze_fii
from utils.helpers import print_key_value_pairs
from utils.helpers import print_banner
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

        print_banner(f"Dados do FII {fii_code.upper()}:")
        print_key_value_pairs(data)
        
        analysis = analyze_fii(data)
        print_banner("Análise do FII:")
        print_key_value_pairs(analysis)

if __name__ == "__main__":
    main()
