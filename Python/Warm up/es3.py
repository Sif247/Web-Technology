#Scrivi uno script che accetta due numeri interi. Se valore di entrambi, la loro somma o
#la loro differenza è 5, stampa “True”, altrimenti stampa “False”. Se gli input inseriti
#non sono numerici, stampa “L’input deve essere un numero.”.

def function(n1,n2):
    try :
        if ((n1 + n2) == 5 or (n1 - n2) == 5 or (n2 - n1) == 5):
            print("true")
        else:
            print("False")
    except:
        print("L’input deve essere un numero.")


function(8,9.2)
function(5,"8")
function(5,10)