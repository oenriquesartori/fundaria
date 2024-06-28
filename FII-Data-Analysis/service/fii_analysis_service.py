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

    def _check_liquidity(self, value):
        if value > 1000000:
            return 'Bom'
        elif 500000 <= value <= 1000000:
            return 'Razoável'
        else:
            return 'Ruim'

    def _check_dividend_yield(self, dy):
        dy_float = float(dy.replace(',', '.').strip('%'))
        if dy_float >= 8:
            return 'Bom'
        elif 5 <= dy_float < 8:
            return 'Razoável'
        else:
            return 'Ruim'

    def _check_pvp(self, pvp):
        pvp_float = float(pvp.replace(',', '.'))
        if pvp_float < 1:
            return 'Bom'
        elif 1 <= pvp_float <= 1.5:
            return 'Razoável'
        else:
            return 'Ruim'

    def _check_monthly_return(self, return_value):
        return_float = float(return_value.replace(',', '.').strip('%'))
        if return_float >= 0:
            return 'Bom'
        else:
            return 'Ruim'
