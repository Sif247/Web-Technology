#Scrivi uno script che accetta una stringa e aggiunge “Sono” davanti alla stessa. Se la
#stringa comincia già con “Sono”, stampa la stringa inalterata

def function(stringa):

    if stringa.startswith("sono") or stringa.startswith("Sono"):
        print(stringa)
    else:
        print("sono " + stringa)

function("sono Isma")
function("Isma Sifdine")