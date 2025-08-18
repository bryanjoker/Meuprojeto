# Conta bancária...

print("Digite o seu saldo:")
saldo = int(input())
print("Digite o valor do produto:")
produto = int(input())

if produto > saldo:
 print("Você não tem saldo suficiente!")
 print("Não poderá relizar esta compra!")
else:
 print("Você tem saldo suficiente!")
 print("Portanto poderá realizar esta compra!")
