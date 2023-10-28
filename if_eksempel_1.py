# Eksempel på if-setning - valg av morgenhilsen

svar = input("Hei, har du en god morgen? Svar J eller N: ")
if svar == "J":
    print("Bra! Gi et smil, og du får 1000 tilbake")
elif svar == "N":
    print("Så leit, håper du snart blir bedre!")
else:
    print("Du svarte noe jeg ikke forstår, ønsker deg en god dag!")
