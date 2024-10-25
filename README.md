# Distribuidora - Análise de Valores Diários

## Descrição
Este projeto lê um arquivo JSON contendo os valores diários de uma distribuidora e realiza análises sobre os dados.

## Funcionalidades
- Cálculo do menor e maior valor de faturamento em um dia.
- Cálculo da média mensal do Faturamento.
- Identificação de quantos dias o valor de faturamento diário foi maior do que a média mensal.

## Estrutura dos Arquivos
- projeto_distribuidora.py:
  ```
    Python principal que realiza a leitura do arquivo dados.json e executa as análises.
- dados.json:
  ```
    Arquivo JSON contendo os valores de faturamento da distribuidora para cada dia do mês.
  
## Funcionalidades
1. Cálculo do Menor e Maior Faturamento:
   - O script identifica os dias com o menor e o maior valor de faturamento dentro dos dados fornecidos.

2. Cálculo da Média de Faturamento:
   - O script calcula a média de faturamento considerando apenas os dias com faturamento superior a zero.

3. Dias com Faturamento Acima da Média:
   - O script conta quantos dias o faturamento foi maior do que a média calculada.
  
## Como Executar
1. Clone o repositório:
   ```
     git clone https://github.com/PauloMPPatricio/distribuidora-de-valores.git
2. Navegue até o diretório do projeto:
   ```
     cd distribuidora-analise-de-valores
4. Certifique-se de que os arquivos "projeto_distribuidora.py" e "dados.json" estão no mesmo diretório.
5. Não esquecer de colocar o diretório do arquivo "dados.json" na linha 68 do código.
6. Execute o script:
   ```
     python projeto_distribuidora.py

## Exemplo de Saída
    Menor valor de faturamento: R$ 373.78 no dia 14
    Maior valor de faturamento: R$ 48924.24 no dia 16
    Número de dias com faturamento acima da média: 10

## Tecnologias Utilizadas
- **Python**
- Bibliotecas:
    - `json` : Usada para ler dados em formato JSON de arquivos ou APIs e convertê-los para objetos Python, como listas ou dicionários, para serem manipulados no código.

## Contribuições
Contribuições são bem-vindas! Se você deseja melhorar este projeto, fique à vontade para abrir issues ou enviar pull requests.

## Licença
Este projeto está licenciado sob a MIT License.



