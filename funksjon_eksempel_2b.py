# Importer modulen random i Python. Når du importerer random, gir det tilgang til funksjoner for å generere tilfeldige tall.
import random

# Definer en funksjon for å kaste terning
def kast_terning():
    resultat = random.randint(1, 6)
    return resultat

# For å kjøre en funksjon må man kalle på funksjonen vi har laget:
kast = kast_terning()

# Til slutt skriver vi ut resultatet, med {kast} som mellomliggende variabel. Vi bruker da noe som heter f-string.
print(f'Du kastet {kast} på terningen')
