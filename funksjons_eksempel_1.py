# Importer modulen random i Python. Når du importerer random, gir det tilgang til funksjoner for å generere tilfeldige tall.
import random

# Definer en funksjon for å kaste terning
def kast_terning():
    resultat = random.randint(1, 6)
    return resultat

# For å kjøre en funksjon må man kalle funksjonen:
kast = kast_terning()

# Til slutt skriver vi ut resultatet, med {kast} som mellomliggende variabel
print(f'Du kastet {kast} på terningen')
