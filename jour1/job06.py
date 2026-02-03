class Animal:
    def __init__(self,age,prenom):
        self.age=age
        self.prenom=prenom
        age=0
    def vieillir(self,):
        self.age +=1
        return self.age
    def nommer(self):
        self.prenom=(input("nomer l'animal :"))
        return self.prenom


chien=Animal(15,"rex")
print("l'age de l'animal est ",chien.age,"ans")
chien.vieillir()
print("l'age de l'animal est ",chien.age,"ans")
print("lanimal s'appel",chien.prenom)
chien.nommer()
print("l'animal s'appel",chien.prenom)

