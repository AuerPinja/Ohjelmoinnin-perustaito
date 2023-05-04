
def tulostaAakkoset():
    aakkoset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
    for i in aakkoset:
        print(i, end = " ")

def tulostaNumerot():
    numerot = [*range(0, 10)]
    for i in numerot:
        print(i, end = " ")

tulostaAakkoset()
tulostaNumerot()