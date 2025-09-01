# demonstrção de acesso a listas...

print("Vou montar a marmita com 5 alimentos!")
Marmita = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, a nossa recomendação:", Marmita)

Resposta = input("Quer monar uma marmita diferente (S/N)?")
if Resposta == "S":
    for X in range(len(Marmita)):
        print(f'Digite o {X+1}o, item do cardápio:')
        Marmita[X] = input()
        print("A marmita montada foi:", Marmita)
        print("O três primeiros itens foram:", Marmita[0:3])
        print("O último item da marmita foi:", Marmita[-1])
else:
    print("Ok, Você decide....")

print(Marmita[:])
print(Marmita[2:3])
print(Marmita[0:4:2])
print(Marmita[-3:-1])