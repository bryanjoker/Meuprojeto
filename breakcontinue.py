# Demonstração de estrututras repetitiva...
contador = 0; senha = ""
while senha != "S3nh4":
    print("Digite sua senha:")
    senha = input()

    if senha == "S3nh4":
        print("SEnha correta!")
    else:
        print("Senha errada...")
    contador += 1
    if contador == 3:
        print("3 tentativas excedidas!")
        break