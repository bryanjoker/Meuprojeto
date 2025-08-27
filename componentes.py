# Demonstrção do uso de funções...
def apresentar():
    print(f"Meu nome é {Myname}.")
    print(f"Minha altura é de {Myheigh} metros.")
    print(f"Minha idade é {Myage} anos. ")
    return
def conferir(X):
    if X >=18:
        print("Você é maior de idade!")
    else:
        print("Ops, menor de idade não pode!")
    return
Myname = str(input("Digite o seu nome: "))
Myheigh = float(input("Digite a sua altura: "))
Myage = int(input("Digite a sua idade: "))

apresentar()
conferir(Myage)