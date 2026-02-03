class Perssonage:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def gauche(self):
        self.x+=1
        return self.x
    def droite(self):
        self.x-=1
        return self.x
    def haut(self):
        self.y-=1
        return self.y
    def bas(self):
        self.y+=1
        return self.y
    def postion(self):
        return (self.x,self.y)
pnj=Perssonage(0,0)
print(pnj.postion())
pnj.gauche()
print(pnj.postion())

