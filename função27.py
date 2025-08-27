# Demonstraçâo do uso de funçôes...
def adição(X, Y):
    W = X + Y
    return W
def subtração(X, Y):
    return X - Y

print("Digite dois valores inteiros...")
N1 = int(input("X: "))
N2 = int(input("Y: "))
OP = input("Qual operação (+ ou -)?")

if OP == "+":
    Z = adição(N1, N2)
    print("Resultado da soma:", Z)
elif OP == "-":
    Z = subtração(N1, N2)
    print("Resultado da subtração:", Z)
else:
    print("Opção digitada inexistente!")