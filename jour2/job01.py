class Rectangle:
    def __init__(self,a,b):
        self.__longueur= a
        self.__largeur= b
    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur
    
    def set__longueur(self,longueur):
        longueur=int(input())
        self.__longueur=longueur
        return self.__longueur
    def set__largeur(self,largeur ):
        largeur= int(input())
        self.__largeur=largeur
        return self.__largeur
rec=Rectangle(10,5)
print(rec.get_largeur())
rec.set__largeur(5)
print(rec.get_largeur())


        