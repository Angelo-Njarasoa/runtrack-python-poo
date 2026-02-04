class Livre:
    def __init__(self,titre,auteur,pages):
        
        self.__auteur=auteur
        self.__titre=titre
        self.__pages=pages
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

book=Livre("dbz","akira",72)
print(book.get_pages())
book.set_pages(72)
print(book.get_pages())
