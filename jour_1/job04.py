class Personne:
    def __init__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
    def Sepresenter(self):
        return f"je suis {self.prenom} {self.nom}"
perso1=Personne("harry","potter")
perso2=Personne("Doe","John")
print(f"je suis",perso2.prenom,perso2.nom)
print(f"je suis",perso1.nom,perso1.prenom)
print(perso1.Sepresenter())