#Dato un numero intero n, esegui le seguenti operazioni condizionali:
#- se n è dispari, stampa “bizzarro”;
#- se n è pari e tra 2 e 5 (compresi), stampa “non bizzarro”;
#- se n è pari e tra 6 e 20 (compresi), stampa “bizzarro”;
#- se n è pari e più grande di 20, stampa “non bizzarro”.

def function(n):
    if n % 2 != 0:
        print("bizzarro")
    elif n >= 2 and n <= 5:
        print("non bizzarro")
    elif n >= 6 and n <= 20:
        print("bizzarro")
    elif n > 20:
        print("non bizzarro")

function(3)
function(4)
function(16)
function(22)