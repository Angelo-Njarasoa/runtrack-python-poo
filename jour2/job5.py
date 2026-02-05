
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False,reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche   # False par défaut grâce au paramètre
        self.__reservoir= reservoir

    # --- Getters (assesseurs) ---
    def reservoire(self):
        return self.__reservoir
    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    # --- Setters (mutateurs) ---
    def set_marque(self, marque):
        self.__marque = marque
        

    def set_modele(self, modele):
        self.__modele = modele

    def set_année(self,annee):
        if annee%1 !=0 :
            return "l'année doit etre un entier"
        else:
            self.__annee= annee
            return self.__annee

    def set_kilometrage(self, kilometrage):
        if kilometrage >= 0:
            self.__kilometrage = kilometrage
        else:
            print("Le kilométrage ne peut pas être négatif")
    
    def set_en_marche(self,en_marche ):
        if en_marche==bool:
            self.__en_marche= en_marche
            return self.__en_marche
        else:
            print("un booleen est attendu (True ou False)")
    def set_resevoir(self,resevoir):
        self.__reservoir=resevoir
        
#---------------------Methodes----------------------------

    def demarrer(self):
        if self.__en_marche == False and self.__verifier_plein()> 5:
            self.__en_marche= True
        else:
            return print("la voiture est deja en marche")
    def arreter(self):
        if self.__en_marche:
            self.__en_marche= False
        else:
            return print("la voiture est deja arreter ")
    def __verifier_plein(self):
        return self.__reservoir

vroom=Voiture("bm","x3",2025,10000,False,6)
vroom.demarrer()
print(vroom.get_en_marche()) 