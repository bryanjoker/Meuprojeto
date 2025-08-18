# Demonstrção do uso de IF...
print("Digite a sua idade:")
idade = int(input())

if idade < 18:
 print("você não é maior de idade!")
 print("Não poderá realizar operações bancárias!")
elif idade >= 65:
 print("Você está aposentado")
 print("Poderemos oferecr suporte técnico...")
else: 
 print("Você é maior de idade. ")
 print("Portanto, poderá realizar a operação. ")

print("Obrigado por escolher os nossos serviços!")