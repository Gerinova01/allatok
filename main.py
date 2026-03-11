from allat import Allat
from allat import Madar
from allat import Keteltu
from allat import Hullo
from emlos import Emlos
from emlos import Macska
from emlos import Kutya

allat1 = Allat("Bodri", "kutya", 5, "kert", "közepes")
allat2 = Allat("Cirmi", "macska", 3, "ház", "közepes")

print(allat1)
print(allat2)

emlos1 = Emlos("Capali", "kutya", 3, "ház", "szürke")
emlos2 = Emlos("Capeti", "macska", 7, "ház", "fekete")

print(emlos1)
print(emlos2)

macska1 = Macska("Hubert", 4, "ház", "fehér")
print(macska1)
macska1.doromboral()

kutya1 = Kutya("Bongyor", 9, "kert", "szürke")
print(kutya1)
kutya1.ugatol()

madar1 = Madar("Csikócsőr")
print(madar1)
madar1.csiripel()

keteltu1 = Keteltu("Zsolti")
print(keteltu1)
keteltu1.brekeg()

hullo1 = Hullo("Megalonia")
print(hullo1)
hullo1.napozik()