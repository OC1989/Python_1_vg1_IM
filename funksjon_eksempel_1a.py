# Importer modulen random i Python. Når du importerer random, gir det tilgang til funksjoner for å generere tilfeldige tall.
import random

# Definer en funksjon for å kaste terning
def kast_terning():
    resultat = random.randint(1, 6)
    return resultat

# Vi skriver ut resultatet av terningkastet
print(
    kast_terning()
)
