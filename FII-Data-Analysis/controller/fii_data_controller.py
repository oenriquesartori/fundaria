"""
Controlador para gerenciar as interações com o usuário relacionadas aos dados dos FIIs.
"""

from service.fii_data_service import FIIDataService

class FIIDataController:
    def __init__(self):
        self.service = FIIDataService()
    
    # get_fii_data(fii_code): Busca os dados do FII especificado.
    def get_fii_data(self, fii_code):
        return self.service.get_fii_data(fii_code)
