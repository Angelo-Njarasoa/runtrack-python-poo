class Point :
    def __init__(self,x,y):
        self.x= x
        self.y= y
        # x=25
        # y=7
    def afficherLesPoints(self):
        return f"coordonée ={self.x}{self.y}"
    def afficherX(self):
        print ("le x = ",self.x)
    def afficherY(self):
        print ("le y = ",self.y)
    def changerX(self):
        self.x=int(input("tapez x : "))
        return self.x
    def changerY(self):
        self.y=int(input("tapez y : "))
        return self.y
p=Point(45,89)
print(p.x)
p.afficherX()
p.changerX()
p.afficherX()
