class Commande:
    def __init__(self,num_de_commande,liste_plat_commande,statut_commande,):
        self.__num_de_commande=num_de_commande
        self.__liste_plat_commande= {"macaroni":{"prix":20,"statut": "en cours"} ,
                                     "salade":{"prix":14,"statut":"termine"},
                                     "cafe":{"prix":2.55,"statut":"en cours"}} #liste_plat_commande
        self.__statut_commande=statut_commande
        #liste_plat_commande={"macaroni":20,"salade":14,"cafe":2.50}
    def add_plat(self,nw_plat,nw_prx,etat):
        st="statut"
        prx="prix"
        self.__liste_plat_commande.update({nw_plat:{prx:nw_prx,st:etat}})
    def annul_commande(self):
        if self.__statut_commande=="annule":
            print("commande deja annule")
        else:
            self.__statut_commande= "annule"
    def get_liste_de_plat_commande(self):
        self.__liste_plat_commande
        return self.__liste_plat_commande
    def prix_total_commande(self):
        #ttls=list(self.__liste_plat_commande.values())
        #2e version:  ttls=[*self.__liste_plat_commande.values()]
        # i=0
        # tt=0
        # while i<len(ttls) :
        #     tt=tt+ttls[i]
        #     i+=1
        #     self.tt=tt
        #return f"commande n°{self.__num_de_commande} prix totale HT :{self.tt} Euros"
        total=0
        
        for  jb,info in self.__liste_plat_commande.items():
            
            total += info["prix"]
            self.tt= total
        return  
    def total_TVA(self):
        tva=self.tt/10
        Prix_totale_tva= self.tt-tva
        return round(Prix_totale_tva,2)
    def compte(self):
        total=0
        
        for  jb,info in self.__liste_plat_commande.items():
            
            total += info["prix"]
         
        return  print(total)  





    
c1= Commande(1,[],"en cours")
c1.compte()
print(c1.get_liste_de_plat_commande())
c1.add_plat("dessert",16,"en cours")
print(c1.get_liste_de_plat_commande())
print(c1.prix_total_commande())
print(c1.total_TVA())









