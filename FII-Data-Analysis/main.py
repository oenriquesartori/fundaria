"""
Arquivo principal do projeto. Gerencia a entrada do usuário e executa a busca e análise dos FIIs.

Funções:
- main(): Função principal que controla o fluxo do programa.
"""

from controller.fii_data_controller import FIIDataController
from controller.fii_analysis_controller import FIIAnalysisController
from utils.helpers import print_key_value_pairs, print_banner
from colorama import init

def main():
    init(autoreset=True) 
    data_controller = FIIDataController()
    analysis_controller = FIIAnalysisController()
    
    while True:
        fii_code = input("Digite o código do FII (ou 'Finalizar' para sair): ").strip().lower()
        
        if fii_code == 'finalizar':
            print("Encerrando o programa...")
            break
        
        data, error = data_controller.get_fii_data(fii_code)
        
        if error:
            print(error)
            continue

        print_banner(f"Dados do FII {fii_code.upper()}:")
        print_key_value_pairs(data)
        
        analysis = analysis_controller.analyze_fii(data)
        print_banner("Análise do FII:")
        print_key_value_pairs(analysis)

if __name__ == "__main__":
    main()
