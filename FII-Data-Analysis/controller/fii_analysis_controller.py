"""
Controlador para gerenciar as interações com o usuário relacionadas à análise dos FIIs.
"""

from service.fii_analysis_service import FIIAnalysisService

class FIIAnalysisController:
    def __init__(self):
        self.service = FIIAnalysisService()
    
    # analyze_fii(data): Analisa os dados do FII especificado.
    def analyze_fii(self, data):
        return self.service.analyze_fii(data)
    
