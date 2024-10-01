# Bibliotecas
import json


class FaturamentoDistribuidora:
    def __init__(self, dados_faturamento):
        self.dados_faturamento = dados_faturamento
        self.faturamento_valido = self.filtrar_faturamento_valido()

    def filtrar_faturamento_valido(self):
        # Filtra os dias com faturamento maior que zero
        return [dia['valor'] for dia in self.dados_faturamento if dia['valor'] > 0]

    def calcular_menor_faturamento(self):
        # Retorna o menor valor de faturamento
        return min(self.faturamento_valido)

    def calcular_maior_faturamento(self):
        # Retorna o maior valor de faturamento
        return max(self.faturamento_valido)

    def calcular_media_faturamento(self):
        # Retorna a média dos valores válidos de faturamento
        return sum(self.faturamento_valido) / len(self.faturamento_valido)

    def dias_acima_da_media(self):
        # Calcula o número de dias com faturamento acima da média
        media = self.calcular_media_faturamento()
        return sum(1 for valor in self.faturamento_valido if valor > media)

    @staticmethod
    def formatar_valor_brasileiro(valor):
        # Formatação manual para padrão brasileiro
        return f'{valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

    def exibir_resultados(self):
        menor_faturamento = self.calcular_menor_faturamento()
        maior_faturamento = self.calcular_maior_faturamento()
        media_faturamento = self.calcular_media_faturamento()
        dias_acima_media = self.dias_acima_da_media()

        # Aplicar formatação manual para padrão brasileiro
        menor_faturamento_fmt = self.formatar_valor_brasileiro(menor_faturamento)
        maior_faturamento_fmt = self.formatar_valor_brasileiro(maior_faturamento)
        media_faturamento_fmt = self.formatar_valor_brasileiro(media_faturamento)

        print(f"Menor faturamento: R$ {menor_faturamento_fmt}")
        print(f"Maior faturamento: R$ {maior_faturamento_fmt}")
        print(f"Média de faturamento: R$ {media_faturamento_fmt}")
        print(f"Dias com faturamento acima da média: {dias_acima_media}")


# Carregar dados do arquivo JSON
with open('/11-Processo Seletivo Target/Faturamento Distribuidora/dados.json', 'r') as file:
    faturamento_data = json.load(file)

# Criar uma instância da classe e chamar o método para exibir os resultados
faturamento = FaturamentoDistribuidora(faturamento_data)
faturamento.exibir_resultados()
