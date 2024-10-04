#Scrivi uno script che accetta un input consistente in un numero intero rappresentante
#un raggio, calcola l’area del rispettivo cerchio e stampa il risultato.

PI = 3.14
def area():
    r = float(input("digit the value of radius: "))

    ris = r * r * PI
    print("l'area è: " + str(ris))
    return ris

area()