Nome = input("Digite seu nome: ")
SM1 = float(input("Digite a SM1: "))
SM2 = float(input("Digite a SM2: "))
AV = float(input("Digite a AV: "))

media = (SM1 + SM2 + AV)
media_F = media

if media >= 6.0:
    status = "Aprovado"
else:
    print(f"A média do {Nome} foi  {media:.1f}, é preciso fazer recuperação.")
    NT = float(input("Digite a NT: "))
    media_F = NT
    if media_F >= 6.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

print(f"A média final do {Nome} foi {media_F:.1f} tendo sido {status}.
