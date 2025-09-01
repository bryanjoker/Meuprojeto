# Seja bem vindo ao rio de janeiro...

def Verificarcidade(N, C):
    if C == "Rio de janeiro":
        print("Olá, ", N)
        print("bem vindo a cidade maravilhosa!")
    else:
        print(N, "Seja bem vindo a", C)

    Nome = input("Digite o seu nome: ")
    Cidade = input("Digite o nome da cidade")
    Verificarcidade(Nome, Cidade)