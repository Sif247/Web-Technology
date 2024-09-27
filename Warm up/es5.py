# Scrivi uno script che accetta un intero n, calcola e stampa il valore di n + n*n + n*n*n

import math
def function(n):
    #first way (without math library)
    #ris = n + (n * n) + (n * n * n)

    #second way (with math library)
    ris = n + pow(n,2) + pow(n,3)
    print(ris)

function(5)
