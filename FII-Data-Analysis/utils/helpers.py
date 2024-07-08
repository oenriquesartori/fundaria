"""
Módulo utilitário com funções auxiliares para o projeto.
"""

from colorama import Fore, Style

def print_key_value_pairs(data):
    color_map = {
        'Bom': Fore.GREEN,
        'Razoável': Fore.YELLOW,
        'Ruim': Fore.RED,
        'Desconhecido': Fore.LIGHTRED_EX,
        'Seguro': Fore.GREEN,
        'Neutro': Fore.YELLOW,
        'Arriscado': Fore.RED,
    }

    for key, value in data.items():
        color = color_map.get(value, Fore.RESET)
        print(f"{key}: {color}{value}{Style.RESET_ALL}")

def print_banner(msg: str, border: str = '-' * 30):
    print(border)
    print(f'    {msg}')
    print(border)
