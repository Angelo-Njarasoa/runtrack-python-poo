class Student:
    def __init__(self,nom,prenom,id,credit,level):
        self.__nom= nom
        self.__prenom=prenom
        self.__id=id
        self.__credit= credit
        self.__level=level
        

    def add_credit(self):
        add= float(input("credit: "))
        if add<0 :
            print("erreur :entrez un nombre positif")
            self.add_credit()
        else:
            self.__credit= int(self.__credit) +int(add)
            return self.__credit
    def get_credit(self):
        return self.__credit
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def get_id(self):
        return self.__id
    def set_nom(self):
        nom=input("nom:")
        self.__nom=nom
        return self.__nom
    def set_prenom(self):
        prenom=input()
        self.__prenom=prenom
        return self.__prenom
    def set_id(self):
        id=float(input("id: "))
        if id % 1 != 0 :
            return print("erreur id doit etre un entier ")
        else:
            self.__id= int(id)
            return self.__id
    
    def __student_Eval(self):
        if self.__credit >= 90 :
            return "Exellent"
        elif self.__credit >=80 :
            return "Tres bien"
        elif self.__credit >= 70:
            return "Bien"
        elif self.__credit >= 60:
            return "passable"
        else:
            return "insuffisant"
    def studentinfo(self):

        print(f"Nom= {self.__nom}\nPrenom= {self.__prenom}\nid= {self.__id}\nNiveau = {self.__student_Eval()}")


    
std=Student("John","Doe",145,0,0)
print(std.get_credit())
std.add_credit()
std.add_credit()
std.add_credit()
print("le nombre de credits de John Doe est", std.get_credit(),"points")
std=Student("John","Doe",145,70,0)
std.studentinfo()




