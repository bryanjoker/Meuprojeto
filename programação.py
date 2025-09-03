# Demonstração de métodos em listas...
Inss = ["maria", "manuel", "josé", "isabela"]
print("Eis, a fila do Inss:", Inss)

Novo = input("Insira mais uma pessoa: ")
Inss.append(Novo)
print("Conferindo a nova lista: ", Inss)

print("Vou tirar a ultima pessoa desta lista...")
Especial = Inss.pop()

print("Agora, vou colocá-la na frente de todos!")
Inss.insert(0, Especial)
print("Conferindo a lista: ", Inss)

print("maria não gostou e reclamou...")
Inss.remove("maria")
print("E agora, ela saiu 'pê da vida'", Inss)

print("Para não ter mais reclamação, vamos atender...")
Inss.sort()
print("... em ordem alfabética:", Inss)

print("Onde está esta nova pessoa chamada", Especial, "?")
print("Ela agora ficou em posição", Inss.index(Especial)+1, "!")