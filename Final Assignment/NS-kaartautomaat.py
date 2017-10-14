def inlezen_beginstation(station):
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
    if any(station in s for s in stations):
        stations.index(station)
    else:
        print(station + " bestaat niet probeer het opnieuw")
        inlezen_beginstation()

def inlezen_eindstation(station, beginstion):
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
    station2 = input("Wat is je beginstation? :")
    eindstation = stations.index(station2)
    if (int(beginstion) < int(eindstation)):
        stations.index(station2)
    else:
        print(station + " bestaat niet probeer het opnieuw")
        inlezen_eindstation()

#def omroepen_reis(station, beginstion, eindstation):
#    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']


station = input("Wat is je beginstation? :")
beginstion = inlezen_beginstation(station)
#eindstation = inlezen_eindstation(station, beginstion)
print(beginstion)
