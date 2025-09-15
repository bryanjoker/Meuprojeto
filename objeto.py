# Confirmação de idade...

class Registro:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
class Registro_2(Registro):
    def apresentar(self):
        print("Olá, sou o", self.nome)
        print("Minha idade é", self.idade)
        print("Minha altura é", self.altura, "centimetros")
        print("Quero acessar minha conta")
        return
    
fulano = Registro_2("Bryan", "18", "180")
fulano.apresentar()
ciclano = Registro_2("caio", "15", "175")
ciclano.apresentar()

# confirmação do registro 
print("De fato, você realmente é:", fulano.nome)
print("Você é maior de idade! possui 18 anos.")

print("De fato, você realmente é:", ciclano.nome)
print("Você é menor! possui 15 anos.")




   