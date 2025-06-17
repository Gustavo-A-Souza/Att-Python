import statistics

# Nome correto do arquivo
caminho_arquivo = 'Text'

try:
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        for i, linha in enumerate(linhas, start=1):
            partes = linha.strip().split(';')

            try:
                # Converte as inforamações para float
                numeros = [float(valor) for valor in partes if valor.strip() != ""]

                if len(numeros) < 2:
                    print(f"\n[Linha {i}] Não há dados suficientes para calcular o desvio padrão.")
                    continue

                # Calculo de Resultados
                media = statistics.mean(numeros)
                mediana = statistics.median(numeros)
                desvio = statistics.stdev(numeros)

                # Resultados
                print(f"\nResultados")
                print("Média:", media)
                print("Mediana:", mediana)
                print("Desvio padrão:", desvio)

            except ValueError:
                print(f"\n[Erro na linha {i}] Dados inválidos. Não foi possível converter para número.")

except FileNotFoundError:
    print("Arquivo 'Text' não encontrado.")