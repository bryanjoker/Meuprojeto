# Demonstração de oop em python

class Cliente:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta 
        self.saldo = saldo
    
class Cliente_fisico(Cliente):
    def apresentar(self):
        print("Olá eu sou:", self.titular)
        print("Minha conta é:", self.conta)
        print("E quero saber o meu saldo,")
        return
    
# Para criar uma instância baseada na classe Cliente...
fulano = Cliente_fisico("João", "432.050285-21", 25000.00)
# Executando o método da instância criada...
fulano.apresentar()

# Acessando os atributos das instâncias criadas...
print("De fato, você realmente é:", fulano.titular)
print("No momento, a sua conta possui R$", fulano.saldo)