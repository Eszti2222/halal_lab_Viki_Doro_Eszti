from Jatekos import Jatekos
import random

def jo_vagy_balszerencse(jatekos, dobas):
    jatekos.szerencse-=1
    if(dobas<jatekos.szerencse):
        valaszt:int=int(input("Ha az ellenfeled sebzésére használod a szerencséd írj be 1-et.Ha védekezésre használod, akkor írj be 2-t: "))

        if(valaszt==1):
            jatekos.ugyesseg*=2 

        else:
            jatekos.eletero=jatekos.eletero-1 #hozzá kell adnunk majd azt a pontszámot , amit a szörny ennél a támadásnűál sebzett rajtunk
    else:
        valaszt:int=int(input("Ha az ellenfeled sebzésére használod a szerencséd írj be 1-et.Ha védekezésre használod, akkor írj be 2-t: "))
        if(valaszt==1):
            jatekos.ugyesseg+=1
        else:
            jatekos.eletero=jatekos.eletero-3 #hozzá kell adnunk majd azt a pontszámot , amit a szörny ennél a támadásnűál sebzett rajtunk
        