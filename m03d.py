inkomst = int(input("Ange din inkomst"))
kommunal = inkomst * 0.2136
landsting = inkomst * 0.1148
arsinkomst = inkomst * 12
statlig = inkomst * 0.2
varnskatt = inkomst * 0.05

bruttot = (1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000)

print("Utskrift")
print("Månadsinkomst      ",(inkomst),("kr"), 'Årsinkomst' ,(arsinkomst),("kr"))
print("Kommunal skatt     ",(kommunal),("kr"))
print("Landstingskatt     ",(landsting),("kr"))

if arsinkomst > 468700 and arsinkomst < 675700:
    print("Statlig skatt      ",(statlig),("kr"))
    print("Kvar efter skatt   ",(inkomst) - (kommunal) - (landsting) - (statlig),("kr"))
    print("Total skatt        ",(kommunal) + (landsting) + (statlig),("kr"))
    print("Total skatt betald ",((kommunal + landsting)/inkomst)*100,("%"));
elif arsinkomst >= 675700:
    print("Statlig skatt      ",(statlig),("kr"))
    print("Värnskatt          ",(varnskatt),("kr"))
    print("Kvar efter skatt   ",(inkomst) - (kommunal) - (landsting) - (statlig) - (varnskatt),("kr"))
    print("Total skatt        ",(kommunal) + (landsting) + (statlig) + (varnskatt),("kr"))
    print("Total skatt betald ",((kommunal + landsting)/inkomst)*100,("%"));
else:
    print("Kvar efter skatt   ",(inkomst) - (kommunal) - (landsting),("kr"))
if arsinkomst <= 19247:
    print("Eftersom du tjänar under brytpunkten betalar du ingen skatt");