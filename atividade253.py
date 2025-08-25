# Melhor clube de fotebol
futebol= 0; resposta = ""
while resposta != "flamengo":
    print("Qual o melhor clube de fotebol no brasil?:")
    resposta = input()

    if resposta == "flamengo":
        print("Parabens, está correto!")
    else:
        print("Opa, você errou...")
    
    if futebol:
        print("tente novamente!")
        break