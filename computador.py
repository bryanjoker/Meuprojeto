# Par ou impar...

def ParImpar(X, Y):
    Resultado = (X + Y) % 2
    if Resultado == 0:
        print("é par! Ser humano venceu!")
    else:
        print("é impar! Computador venceu!")

N1 = int(input("Computador - digite um numero: "))
N2 = int(input("Ser humano - digite um numero: "))
ParImpar(N1, N2)