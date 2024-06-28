"""
Serviço para gerenciar a lógica de negócios relacionada à busca dos dados dos FIIs.
"""

from repository.fii_data_repository import FIIDataRepository

class FIIDataService:
    def __init__(self):
        self.repository = FIIDataRepository()

    # get_fii_data(fii_code): Busca os dados do FII especificado.
    def get_fii_data(self, fii_code):
        return self.repository.fetch_fii_data(fii_code)
