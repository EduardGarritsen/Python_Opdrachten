cijferICOR = 6
cijferPROG = 7
cijferCSN = 8

gemiddelde = ((cijferICOR + cijferPROG + cijferCSN) / 3)
beloning = gemiddelde * 30
overzicht = 'mijn cijfers gemiddeld is ' + str(gemiddelde) + ' en dat levert een beloning van ' + str(beloning) + 'euro op!'
print(overzicht)
