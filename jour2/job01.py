class Rectangle:
    def __init__(self,a,b):
        self.__longueur= a
        self.__largeur= b
    def get_longueur(self):
        return f"la longueur est {self.__longueur}"
    def get_largeur(self):
        return f"la largeur est {self.__largeur}"
    
    def set__longueur(self,longueur):
        longueur=int(input("longueur: "))
        self.__longueur=longueur
        return self.__longueur
    def set__largeur(self,largeur ):
        largeur= int(input("largeur: "))
        self.__largeur=largeur
        return self.__largeur
rec=Rectangle(10,5)
print(rec.get_largeur())
print(rec.get_longueur())
rec.set__largeur(5)
rec.set__longueur(10)

print(rec.get_largeur())
print(rec.get_longueur())




        