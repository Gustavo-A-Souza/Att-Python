Nome = input("Digite seu nome: ")
SM1 = float(input("Digite a SM1: "))
SM2 = float(input("Digite a SM2: "))
AV = float(input("Digite a AV: "))

media = (SM1 + SM2 + AV)

if media >= 6.0:
    media_F = media
    status = "Aprovado"
else:
    status = "Re-provado"
print(f"A média final do {Nome} foi {media_F:.1f} tendo sido {status}.")