# Eksempel på en for-løkke som utfører en matematisk operasjon og oppdaterer en liste

# Lag en liste med tall
liste = [2, 4, 6, 8, 10]

# Opprett en tom liste for å lagre de doblede tallene
dobbelte_tall = []

# Bruk en for-løkke til å doble hvert tall i listen og legg dem til i den nye listen
for element in liste:
    doblet_tall = element * 2
    dobbelte_tall.append(doblet_tall)

# Skriv ut den oppdaterte listen med de doblede tallene
print(dobbelte_tall)
