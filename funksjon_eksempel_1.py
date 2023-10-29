# Definer en funksjon for å lage en hilsen
def lag_hilsen(navn):
    hilsen = "Hei, " + navn + "!"
    return hilsen

# Spør brukeren om navnet deres
navn = input("Hva er navnet ditt? ")

# Kall funksjonen for å lage hilsen. Vi setter også inn 'navn' som argument, for å sende informasjonen inn i funksjonen.
hilsen = lag_hilsen(navn)

# Vis hilsenen
print(hilsen)
