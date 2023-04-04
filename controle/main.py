creno1 = ((8,30),(9,30))
creno2 = ((9,30),(10,30))
creno3 = ((10,30),(10,45))

creno4 = ((10,20),(11,30))

planning = []

#1.1
def conflitAvec(creno1,creno2):
    if creno1[0] <= creno2[0] and creno1[1] <= creno2[0]:
        return False
    elif creno1[0] >= creno2[0] and creno1[0] >= creno2[1]:
        return False
    else:
        return True
#1.2
def duree(creno):
    temps = (creno[1][0] - creno[0][0]) * 60 + (creno[1][1] - creno[0][1])
    return temps

#2.1      
def ajouterCreneau(creno,planning):
    for i in range(len(planning)):
        if conflitAvec(creno,planning[i]):
            return False
    planning.append(creno)
    return True

#2.2
def afficher(planning):
    for i in range(len(planning)):
        print('Creneau',i+1,':',planning[i])
        
#2.3
def dureeTotale(planning):
    temps = 0
    for i in range(len(planning)):
        temps += duree(planning[i])
    return temps

#2.4
def dureeTotaleHM(planning):
    temps = 0
    for i in range(len(planning)):
        temps += duree(planning[i])
    heures = temps // 60
    minutes = temps % 60
    temps = (heures,minutes)
    return temps

#3
def tests():
    
    assert conflitAvec(creno1,creno2) == False
    assert conflitAvec(creno2,creno3) == False
    assert conflitAvec(creno1,creno4) == False
    assert conflitAvec(creno2,creno4) == True
    assert conflitAvec(creno3,creno4) == True
    
    assert duree(creno1) == 60
    assert duree(creno2) == 60
    assert duree(creno3) == 15
    assert duree(creno4) == 70
    
    assert ajouterCreneau(creno1,planning) == True
    assert ajouterCreneau(creno2,planning) == True
    assert ajouterCreneau(creno3,planning) == True
    assert ajouterCreneau(creno4,planning) == False
    
    assert dureeTotale(planning) == 135
    assert dureeTotaleHM(planning) == (2,15)
    
    print('Tests OK')

tests()