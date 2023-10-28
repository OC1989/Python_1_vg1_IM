# Dette er et eksempel på en while-løkke som ber brukeren om å gjette et tall

# Generer et tilfeldig tall mellom 1 og 10
import random
hemmelig_tall = random.randint(1, 10)

# Initialiser en variabel for brukerens gjetninger
gjett = 0

# Start en while-løkke som kjører så lenge brukeren ikke har gjettet riktig
while gjett != hemmelig_tall:
    gjett = int(input("Gjett tallet (mellom 1 og 10): ")  # Spør brukeren om å gjette et tall
    
    if gjett == hemmelig_tall:
        print("Gratulerer, du gjettet riktig!")
    else:
        print("Beklager, prøv igjen.")

# Utskrift når løkken er ferdig
print("Spillet er ferdig.")
