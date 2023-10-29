# Definer en funksjon for å lage en hilsen
def lag_hilsen(navn):
    hilsen = "Hei, " + navn + "!"
    return hilsen

# Spør brukeren om navnet deres
navn = input("Hva er navnet ditt? ")

# Kall funksjonen for å lage hilsen, der vi har satt inn "navn" som argument.
hilsen = lag_hilsen(navn)

# Vis hilsenen
print(hilsen)
