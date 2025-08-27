# Demonstraçâo do uso de funçôes...
def adição(X, Y):
    W = X + Y
    return W
def subtração(X, Y):
    return X - Y
def multiplicação(X, Y):
    W = X * Y
    return W
def divisão(X, Y):
    return X / Y

print("Digite dois valores inteiros...")
N1 = int(input("X: "))
N2 = int(input("Y: "))
OP = input("Qual operação (+ ou - ou * ou /)")

if OP == "+":
    Z = adição(N1, N2)
    print("Resultado da soma:", Z)
elif OP == "-":
    Z = subtração(N1, N2)
    print("Resultado da subtração:", Z)
elif OP == "*":
    Z = multiplicação(N1, N2)
    print("Resultado da multiplicação:", Z)
elif OP == "/":
    Z = divisão(N1, N2)
    print("Resultado da divisão:", Z)
else:
    print("Opção digitada inexistente!")