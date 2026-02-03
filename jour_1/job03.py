class opération:
    def __init__(self,nombre1,nombre2):
        self.nombre1=nombre1
        self.nombre2=nombre2
    def addition(self,nombre1,nombre2):
        value=nombre1+nombre2
        return value
p=opération(None,None)

print(p.addition(48,3))