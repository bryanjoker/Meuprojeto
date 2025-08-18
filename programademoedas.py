# Demonstração do uso da condicional match/case...
print("Digite o múmero referente ao estado da moeda:")
print("1, Flor de cunho")
print("2, Soberba")
print("3, Muito bem conservada")
print("4, bem conservada")
print("5, OUtros estados")
estado = int(input())

match estado:
    case 1:
        print("Perfeita! vou pagar R$ 1.000.000.00!")
    case 2:
        print("Quase perfeita! ofereço R$ 250.000.00!")
    case 3:
        print("Que ótimo! posso dar uns R$ 100.000.00!")
    case 4:
        print("Que bom. Aceitaria 30.000.00?")    
    case 5:
        print("Desculpe, não aceito neste estado.")   
    case _:     
        print("Opção não recohecida!")