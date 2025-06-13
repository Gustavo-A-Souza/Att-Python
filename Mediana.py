import statistics #Facilita no Calculo da Mediana

Numeros = []

while True:
    Text = input("Digite um número (Pressione Enter Para Finalizar): ") #Captura os Valores da Mediana
    if Text == "":
        break #Finaliza a captura de valores
    try:
        Numero = float(Text) #Define o valor de Numeros para float
        Numeros.append(Numero)
    except ValueError:
        print("Valor Digitado é Invalido") #Casso valor seja incorreto

if Numeros:
    Mediana = statistics.median(Numeros) #Calcula a mediana
    print("Sua mediana é:", Mediana) #Apresenta Valor da Mediana
else:
    print("Sem Informações para Mediana") #Casso não haja valor