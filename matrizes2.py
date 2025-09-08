# Demonstrção de matrizes em python...
print("Eis, o teclado número do terminal:")
teclado = [[1, 2, 3],
           [4, 5, 6],                             
           [7, 8, 9]]
Senha = []

print("Digite a sua senha de 4 dígitos...")
for X in range(0, 4):
    Senha.append(int(input(f'Digite o dígito {X+1}: ')))

for X in range(0, 3):
    for Y in range(0, 3):
        for Z in range(0, 4):
            if teclado[X][Y] == Senha[Z]:
                teclado[X][Y] = 0

print("Eis, a senha digitada: ", Senha)
print("Confira, as teclas acionadas:")
for listas in teclado:
    print(listas)