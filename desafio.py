# Meu clube do coração

Naturalidade = input("Qual é a sua naturalidade? ")

if Naturalidade == "carioca":
    Time = input("Qual é o seu time? ")
    match Time:
        case "flamengo":
            print("Parabén! você é um privilegiado!")
        case "fluminenese":
            print("Não vou sacanear os tricolores...")
        case "vasco":
            print("Não vou sacanear os vascaínos...")
        case "botafogo":
            print("Não vou sacanear os botafoguenses...")
        case _:
            print("Este time não é nenhum dos grandes do rio!")
elif Naturalidade == "mineiro":
    Time = input("Qual é o seu time? ")
    match Time:
        case "cruzeiro":
            print("Parabén! você é um privilegiado!")
        case "villa nova":
            print("Não vou sacanear os vilanovenses...")
        case "pouso alegre":
            print("Não vou sacanear os pousoalegrence...")
        case "atletico mineiro":
            print("Não vou sacanear os atleticanos...")
        case _:
            print("Este time não é nenhum dos grandes de minas!")
elif Naturalidade == "paulista":
    Time = input("Qual é o seu time? ")
    match Time:
        case "são paulo":
            print("Parabén! você é um privilegiado!")
        case "palmeiras":
            print("Não vou sacanear os palmeirences...")
        case "santos":
            print("Não vou sacanear os santistas...")
        case "corinthias":
            print("Não vou sacanear os corinthianos...")
        case _:
            print("Este time não é nenhum dos grandes de são paulo!")


