import random

class Jatekos:
    def __init__(self,nev:str, ugyesseg:int, eletero:int, szerencse:int):
        self.nev = nev
        self.ugyesseg = ugyesseg
        self.eletero = eletero
        self.szerencse = szerencse
        self.set_ugyesseg()  
        self.set_eletero()  
        self.set_szerencse()
        
    def __str__(self):
        return f"A játékos neve: {self.nev},ügyessége: {self.ugyesseg}, életereje: {self.eletero}, szerencséje: {self.szerencse}" 

    def dobas(self):
        dobas = int(random.random() * 6 + 1)
        return dobas
    
    def set_ugyesseg(self):
        dobas= self.dobas()
        self.ugyesseg+=dobas+6

    def set_eletero(self):
        dobas =2*self.dobas()
        self.eletero +=dobas+12 

    def set_szerencse(self):
        dobas = self.dobas()
        self.szerencse +=dobas+6

    def kiir(self):
        print(f"Ügyesség: {self.ugyesseg}, Életerő: {self.eletero}, Szerencse: {self.szerencse}")

    
    