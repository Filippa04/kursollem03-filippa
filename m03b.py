inkomst = int(input("Ange din månadslön: "))

kommunal = 0.2136
landsting = 0.1148
netto1 = inkomst * kommunal
netto2 = inkomst * landsting
arsinkomst = inkomst * 12

print("Utskrift")
print("Månadslön          ",(inkomst)     , "Årsinkomst ",(arsinkomst))
print("Kommunal skatt     ",(netto1))
print("Landstingsskatt    ",(netto2))
print("Kvar efter skatt   ",(inkomst) - (netto1) - (netto2))

if arsinkomst <= 19247:
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt");
