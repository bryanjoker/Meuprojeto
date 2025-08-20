# Demonstração de operadores lógicos em condicionais 
print("O que você vai fazer amanhã de manhã?")
print("dormir / estudar / planejar")
manha = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar / treinar / trabalhar")
tarde = input()

if manha == "dormir":
 print("Você está desperdiçando o seu dia!")
if tarde == "jogar":
 print("Você está desperdiçando o seu dia!")

if manha == "estudar":
 print("Que bom! você irá se aperfeiçoar!")
if tarde == "treinar":
 print("que bom! você irá se aperfeiçoar!")

if manha == "planejar":
 if tarde == "trabalhar":
   print("Para trabalhar melhor, devo planejar!")

   print("Tenha um bom dia!")