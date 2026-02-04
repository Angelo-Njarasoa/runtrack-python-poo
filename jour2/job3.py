class Livre:
    def __init__(self,titre,auteur,pages,disponible):
        
        self.__auteur=auteur
        self.__titre=titre
        self.__pages=pages
        self.__disponible= disponible
        disponible=False
    def get_auteur(self):
        return self.__auteur
    def get_titre(self):
        return self.__titre
    def get_pages(self):
        return self.__pages
    
    def set_auteur(self,auteur):
        auteur=input()
        self.__auteur=auteur
        return self.__auteur
    def set_titre(self,titre):
        titre=input()
        self.__titre=titre
        return self.__titre
    def set_pages(self,pages):
            pages=float(input())
            if pages %1 > 0 :
                print("error pages must be integer")
                
            else:
                self.__pages=pages
                return self.__pages
    def vérification(self):
        if self.__disponible :
            return True
        else:
            return False
    def emprunter(self):
        if self.__disponible:
            self.__disponible==False
        else:
            return print("le livre n'est pas disponible")
    def rendre(self):
        if self.__disponible== False:
            self.__disponible==True
        else:
            return print("le livre n'est pas emprunté il est deja disponible")
        
    
    
    

book=Livre("dbz","akira",72,True)
book.rendre()
print(book.get_pages())
book.set_pages(72)
print(book.get_pages())
print(book.vérification())