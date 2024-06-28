"""
Módulo utilitário com funções auxiliares para o projeto.

Funções:
- print_key_value_pairs(data): Imprime os pares chave-valor de um dicionário formatados.
"""

def print_key_value_pairs(data):
    for key, value in data.items():
        print(f"{key}: {value}")


def print_banner(msg: str, border: str = '-' * 30):
    print(border)
    print(f'    {msg}')
    print(border)
