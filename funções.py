# demonstrção de funções em listas...
print("Eis, os meus maiores sonhos...")
Sonhos = ["1, Me divertir na disney",
          "2, Me banhar na praia de sepetiba",
          "3, Tirar as férias em paris",
          "4, Fazer compras no westshopping",
          "5, Ver as pirâmides do egito"]
for X in Sonhos:
    print(X)

print("Ops, não quero sepetiba!")
del(Sonhos[1])
print("E nem westshopping...")
del(Sonhos[3])

print("Conferindo os sonhos...")
for X in Sonhos:
    print(X)