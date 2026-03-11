from allat import Allat
from allat import Madar
from allat import Keteltu
from allat import Hullo
from emlos import Emlos
from emlos import Macska
from emlos import Kutya


allatok = []
with open("adatok/allatok.txt", "r", encoding="utf-8") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, faj, eletkor, szorzet_szine = sor.strip().split(',')

        if faj == "kutya":
            allatok.append(Kutya(nev, int(eletkor), "udvar", szorzet_szine))
        elif faj == "macska":
            allatok.append(Macska(nev, int(eletkor), "ház", szorzet_szine))
        elif faj == "madar":
            allatok.append(Madar(nev))
        elif faj == "keteltu":
            allatok.append(Keteltu(nev))
        elif faj == "hullo":
            allatok.append(Hullo(nev))



for allat in allatok:
    print(allat)
    if isinstance(allat,Kutya):
        allat.ugatol()
    elif isinstance(allat,Macska):
        allat.doromboral()
    elif isinstance(allat,Madar):
        allat.csiripel()
    elif isinstance(allat,Keteltu):
        allat.brekeg()
    elif isinstance(allat,Hullo):
        allat.napozik()
