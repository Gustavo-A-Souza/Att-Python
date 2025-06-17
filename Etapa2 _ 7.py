#Procura do Arquivo
caminho_arquivo = 'Text'

try:
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        for i, linha in enumerate(linhas, start=1):
            partes = linha.strip().split(';')

            if len(partes) != 5:
                print(f"[Linha {i}] Dados incompletos: {linha.strip()}")
                continue

            nome = partes[0].strip()
            try:
                sm1 = float(partes[1])
                sm2 = float(partes[2])
                av = float(partes[3])
                nt = float(partes[4])

                # Cálculo de resultados
                media_final = (sm1 + sm2 + av) * 0.7 + nt * 0.3

                # Verificação de satus
                status = "aprovado" if media_final >= 6.0 else "reprovado"

                # Resultado
                print(f"A média final do aluno {nome} foi {media_final:.1f} tendo sido {status}.")

            except ValueError:
                print(f"[Linha {i}] Erro ao converter nota para número: {linha.strip()}")

except FileNotFoundError:
    print(f"Arquivo '{caminho_arquivo}' não encontrado.")