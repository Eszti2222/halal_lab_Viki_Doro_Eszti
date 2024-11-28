import random
class HarcMenete:

    '''
    1.  Dobj két kockával a teremtmény nevében.
        A kapott számot add az ő ÜGYESSÉG pontjaihoz.
        Az összeg az ő TÁMADÓEREJE.

    2.  Dobj két kockával most magadnak,
        és az eredményt add saját jelenlegi ÜGYESSÉG pontjaidhoz.
        Ez a te TÁMADÓERŐD.
    '''
    def tamadoeroGeneral(self):     #->main-ben 2x meghivni-> ellenfelnek + a jatekosnak generalunk tamado erot
        # 2 kockával dob számának legenerálása
        dobas:int=int(random.random()*11+2)

        tEro:int= dobas # + ÜGYESSÉGpontjai     ->ügyességp main-ben paraméterlént,def zárójelbe rakni!!!
        # return tEro


    '''
    3.  Ha a te TÁMADÓERŐD nagyobb, mint a teremtményé, akivel küzdesz, megsebezted.
        Menj tovább a 4. lépésre.
        Ha a teremtmény TÁMADÓEREJE nagyobb, ő sebzett meg téged, és haladj az
        5. lépéshez. Ha a két TÁMADÓERŐ egyforma, kivédtétek egymáscsapását,
        és a következő Fordulót az 1. lépéstől elölről kezditek. 
    '''