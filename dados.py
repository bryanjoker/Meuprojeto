# Demonstração o uso de listas ...
opção = 999
series = []; serviços = []; temporadas = []
while opção != 0:
    print("Escolha a operação")
    print("1. cadastrar / 2. exibir / 3. editar / 4. excluir")
    opção = int(input("Digite 0 para sair: "))

    if opção == 1:
        serie = input("Digite o nome da série: ")
        serviço = input("Digite o nome do serviço: ")
        temporada = input("Digite a temporada que já assistiu: ")
        series.append(serie); serviços.append(serviço); temporadas.append(temporada)
   
        opção == 2
        print(f'Você assistiu apenas a', [temporada], [serie])

print(series, serviços, temporadas)

# É possivél personalizá-lo para adicionar funções extras?