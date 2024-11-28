from Kezdoertek import Jatekos
import random

def jo_vagy_balszerencse(ugyesseg,eletero,szerencse):
    szerencses_sebzes=0
    szerencses_vedekezes=0
    balszerencses_sebzes=0
    balszerencses_vedekezes=0
    i:int=0
    kocka_dob=0
    while(i<2):
        kocka_dob+= int(random.random()*6+1)
        i+=1
    if(kocka_dob<szerencse):
        szerencse-=1
        szerencses_sebzes=ugyesseg*2 
        szerencses_vedekezes
        
    else:
        szerencse-=1
        balszerencses_sebzes+=1
        balszerencses_vedekezes+=1