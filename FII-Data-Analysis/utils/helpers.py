"""
Módulo utilitário com funções auxiliares para o projeto.

Funções:
- print_key_value_pairs(data): Imprime os pares chave-valor de um dicionário formatados.
"""

def print_key_value_pairs(data):
    for key, value in data.items():
        print(f"{key}: {value}")


def bunitu(msg):
    print('-'*30)
    print('   ', msg)
    print('-'*30)
