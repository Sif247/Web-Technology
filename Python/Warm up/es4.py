#Scrivi uno script che accetta un input con nome e cognome e stampa la stringa con i
#caratteri di “index” dispari in ordine inverso.

def function():
    name = input("digit your name: ")
    surname = input("digit your surname: ")
    ris = ""
    i = len(name) - 1
    j = len(surname) - 1
    while i > 0:
        if (i % 2) != 0:
            ris += name[i]
        i -= 1


    while j > 0:
        if (j % 2) != 0:
            ris += surname[j]
        j -= 1

    print(ris)


function()