import statistics  # Facilita o cálculo da média e mediana

numeros = []

# Coleta os números digitados
while True:
    texto = input("Digite um número (pressione Enter para finalizar): ")
    if texto == "":
        break
    try:
        numero = float(texto)
        numeros.append(numero)
    except ValueError:
        print("Valor digitado é inválido.")

# Verifica se há números para calcular
if numeros:
    desvio = statistics.stdev(numeros)
    print("Quantidade de números inseridos:", len(numeros))
    print("Desvio Padrão:", desvio)
else:
    print("Sem informações suficientes para cálculo.")