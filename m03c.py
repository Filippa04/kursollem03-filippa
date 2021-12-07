inkomst = int(input("Ange din inkomst"))
kommunal = inkomst * 0.2136
landsting = inkomst * 0.1148
arsinkomst = inkomst * 12
statlig = inkomst * 0.2
varnskatt = inkomst * 0.05

print("Utskrift")
print("Månadsinkomst      ",(inkomst), 'Årsinkomst' ,(arsinkomst))
print("Kommunal skatt     ",(kommunal))
print("Landstingskatt     ",(landsting))

if arsinkomst > 468700 and arsinkomst < 675700:
    print("Statlig skatt      ",(statlig))
    print("Kvar efter skatt   ",(inkomst) - (kommunal) - (landsting) - (statlig))

elif arsinkomst >= 675700:
    print("Statlig skatt      ",(statlig))
    print("Värnskatt          ",(varnskatt))
    print("Kvar efter skatt   ",(inkomst) - (kommunal) - (landsting) - (statlig) - (varnskatt));
else:
    print("Kvar efter skatt   ",(inkomst) - (kommunal) - (landsting))

if arsinkomst <= 19247:
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt");
