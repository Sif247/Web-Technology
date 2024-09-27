#Scrivi uno script che calcoli la differenza tra un numero dato e 17. Se il numero è
#minore di 17, stampa il doppio della differenza assoluta (Python possiede la funzione
#abs(n) che ritorna il valore assoluto di un int o float).

NUM = 17
def function(n):
    if n < NUM:
        ris = 2 * abs(n - NUM)
        print(ris)
    else:
        print("the number is bigger than 17")

function(5)
function(16)
function(63)
