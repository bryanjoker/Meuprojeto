# Loja de carros 

def verificaridade(X):
    if X < 18:
        print("Teletubies, desenhos animados, os anjinhos")
    else:
        print("Monza: R$ 15.000, R$ 18.000, Fusca: R$ 10.000...")

idade = int(input("Digite sua idade:")) 
verificaridade(idade)