class Allat:
    def __init__(self,nev, faj, eletkor, elohely, meret):
        self.nev = nev
        self.faj = faj
        self.eletkor = eletkor
        self.elohely = elohely
        self.meret = meret

    def __str__(self):
        return f"{self.nev} {self.faj} {self.eletkor} éves élőhelye {self.elohely}"