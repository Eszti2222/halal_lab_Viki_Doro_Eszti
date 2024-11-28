import random

class Jatekos:
    def __init__(self,nev:str, ugyesseg:int, eletero:int, szerencse:int):
        self.ugyesseg = ugyesseg
        self.eletero = eletero
        self.szerencse = szerencse
        self.nev = nev
        self.ertekadas()
        
    def __str__(self):
        return f"A játékos neve: {self.nev},ügyessége: {self.ugyesseg}, életereje: {self.eletero}, szerencséje: {self.szerencse}" 

    def ertekadas(self):
        dobas_ugyi:int=int(random.random()*6+1)
        dobas_elet:int=int(random.random()*6+1)
        dobas_elet2:int=int(random.random()*6+1)
        dobas_szer:int=int(random.random()*6+1)

        self.ugyesseg:int=dobas_ugyi+6
        self.eletero:int=dobas_elet+dobas_elet2+12
        self.szerencse:int=dobas_szer+6
    
    