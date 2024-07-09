"""
Serviço para gerenciar a lógica de negócios relacionada à análise dos FIIs.
"""

class FIIAnalysisService:
    def analyze_fii(self, data):
        analysis = {}

        # Liquidez Média Diária
        liquidez_media_diaria_str = data.get("Liquidez Média Diária", "")
        liquidez_media_diaria = self._convert_to_float(liquidez_media_diaria_str)
        if liquidez_media_diaria is not None:
            analysis['Liquidez Média Diária'] = self._check_liquidity(liquidez_media_diaria)
        else:
            analysis['Liquidez Média Diária'] = 'Desconhecido'

        # Dividend Yield
        try:
            dividend_yield = data.get("Dividend Yield", "")
            analysis['Dividend Yield'] = self._check_dividend_yield(dividend_yield)
        except ValueError:
            analysis['Dividend Yield'] = 'Desconhecido'

        # Patrimônio Líquido
        patrimonio_liquido_str = data.get("Patrimônio Líquido", "")
        patrimonio_liquido = self.converter(patrimonio_liquido_str)
        if patrimonio_liquido is not None:
            analysis['Patrimônio Líquido'] = self._check_patrimonio_liquido(patrimonio_liquido)
        else:
            analysis['Patrimônio Líquido'] = 'Desconhecido'

        # Valor Patrimonial (P/VP)
        try:
            pvp = data.get("P/VP", "")
            analysis['P/VP'] = self._check_pvp(pvp)
        except ValueError:
            analysis['P/VP'] = 'Desconhecido'

        # Análise do Risco com base nos critérios combinados
        criterios = ['Liquidez Média Diária', 'Dividend Yield', 'Patrimônio Líquido', 'P/VP']
        avaliacao = {'Bom': 2, 'Razoável': 1, 'Ruim': 0}

        pontuacao_total = sum(avaliacao.get(analysis.get(criterio, ''), 0) for criterio in criterios)

        if pontuacao_total == 8:
            risk = 'Seguro'
        elif 5 <= pontuacao_total < 8:
            risk = 'Neutro'
        else:
            risk = 'Arriscado'

        analysis['Risco'] = risk

        return analysis
    
    # Métodos para análise
    def _convert_to_float(self, value_str):
        try:
            value_str = value_str.strip().replace('.', '').replace(',', '.')
            
            if value_str.endswith('K'):
                return float(value_str[:-1]) * 1_000
            elif value_str.endswith('M'):
                return float(value_str[:-1]) * 1_000_000
            elif value_str.endswith('B'):
                return float(value_str[:-1]) * 1_000_000_000
            else:
                return float(value_str)
        except ValueError:
            return None

    def converter(self, value_str):
        try:
            value_str = value_str.strip().replace('.', '').replace(',', '.').replace('R$', '').strip()

            if value_str.endswith('K'):
                return float(value_str[:-1]) * 1_000
            elif value_str.endswith('M'):
                return float(value_str[:-1]) * 1_000_000
            elif value_str.endswith('B'):
                return float(value_str[:-1]) * 1_000_000_000
            else:
                return float(value_str)
        except ValueError:
            return None

    def _check_patrimonio_liquido(self, value):
        if value >= 3000000000:
            return 'Bom'
        elif 1000000000 <= value < 3000000000:
            return 'Razoável'
        else:
            return 'Ruim'

    def _check_liquidity(self, value):
        if value > 1000000:
            return 'Bom'
        elif 500000 <= value <= 1000000:
            return 'Razoável'
        else:
            return 'Ruim'

    def _check_dividend_yield(self, dy):
        dy_float = float(dy.replace(',', '.').strip('%'))
        if dy_float >= 6:
            return 'Bom'
        elif 4 <= dy_float < 6:
            return 'Razoável'
        else:
            return 'Ruim'

    def _check_pvp(self, pvp):
        pvp_float = float(pvp.replace(',', '.'))
        if pvp_float < 1:
            return 'Bom'
        elif 1 <= pvp_float <= 1.2:
            return 'Razoável'
        else:
            return 'Ruim'
