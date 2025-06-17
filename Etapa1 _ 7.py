Nome = input("Digite seu nome: ")
SM1 = float(input("Digite a SM1: "))
SM2 = float(input("Digite a SM2: "))
AV = float(input("Digite a AV: "))
NT = float(input("Digite a NT: "))
    
media_Inicial = (SM1 + SM2 + AV)*0.7 + NT*0.3

if media_Inicial >= 6.0:
    status = "Aprovado"
else:
    status = "Reprovado"

print(f"A média final do {Nome} foi {media_Inicial:.1f} tendo sido {status}.")
