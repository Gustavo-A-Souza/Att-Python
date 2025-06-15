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
    desvio = statistics.stdev(numeros) #Calcula o desvio
    Média =  statistics.mean(numeros) #Calcula a média
    Mediana = statistics.median(numeros) #Calcula a mediana
    print("Sua mediana é:", Mediana) #Apresenta Valor da Mediana
    print("Sua média é:", Média) #Apresenta o Valor da Média
    print("Desvio Padrão:", desvio)
    print("Quantidade de números inseridos:", len(numeros))
else:
    print("Sem informações suficientes para cálculo.")
