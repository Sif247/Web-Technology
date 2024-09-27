#Scrivi uno script che accetta tre numeri interi. Se sono tutti diversi, stampa la somma
#dei tre; se due sono uguali, stampa il risultato della somma di quelli uguali divisi per il
#terzo; se tutti e tre sono uguali, stampa il risultato di (n + n)n.

def function(n1,n2,n3):
    if (n1 != n2) and (n2 != n3) and (n1 != n3) :
        print(n1 + n2 + n3)
    elif (n1 == n2) and (n2 == n3):
        print((n1 + n1)*(n1 + n1))
    else:
        if n1 == n2:
            print((n1 + n2) / n3)
        elif n2 == n3:
            print((n2 + n3) / n1)
        else:
            print((n3 + n1) / n2)

function(5,8,5)
