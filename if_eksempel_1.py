# Dette programmet spør brukeren om alderen deres og gir en tilbakemelding basert på svaret.

# Spør brukeren om alderen
alder = int(input("Hvor gammel er du? "))

# Sjekk alderen og gi en tilbakemelding
if alder < 18:
    print("Du er ikke myndig.")
else:
    print("Du er myndig.")

# Programmet avsluttes
