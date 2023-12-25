class Bakal():
    def __init__(self, leb,brasno,vino,mleko):
        self.leb=leb
        self.brasno=brasno
        self.vino=vino
        self.mleko=mleko
P1=Bakal("35 den "," 20 den 1kg","smedervka 120 den","56 den 1l")
print(P1.vino)
print("cena leb",P1.leb ,P1.brasno)
p2=Bakal("34 den","23 den 1kg","vranec 125 den","60 den 1l ")
print("cena vino",p2.vino,"cena leb",p2.leb)