import Harcmenete
import Jatekmenet
from Kezdoertek import Jatekos
from Szerencseprobaja import jo_vagy_balszerencse

labirintus=Jatekmenet.labirintus_generalasa()
jatekos=Jatekos(6,6,6)#jatekos generalasa
Jatekmenet.jatek(labirintus, jatekos)
