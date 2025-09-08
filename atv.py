# Rotina de escalação para 11 jogadores...

numbers = []
players = []
for x in range(0, 11):
    numero = input("Digite a camisa: ")
    numbers.append(numero)
    jogador = input("Digite o nome do jogador: ")
    players.append(jogador)
print(numbers, players)

# Rotina de subtstituição de jogadores...

Y = 0
substituição = "S"
while substituição == "S":
 saida = input("Digite o numero de saida: ")
 jogador = input("Digite o nome de entrada: ")
 jogador = input("Digite o nome do jogador: ")
 for X in range(0, 11):
    if numbers[X] == saida:
        numbers[X]
        players [X] = jogador
    else:
       
     print(numbers, players)
 Y = Y + 1
 if Y == 3:
    substituição = input("Deseja substituir mais (S/N): ")
# Exibição dos substitutos...
print(numbers, players)

