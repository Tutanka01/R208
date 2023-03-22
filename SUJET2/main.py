les_personnes = []
lien_parente = []

#1
def ajout(tab, nom, prenom, sexe, date):
    tab.append([nom, prenom, sexe, date])
    return tab
#2
def affichage(tab):
    for i in range(len(tab)):
        print("La personne d'indice {} est :".format(i), tab[i])
#3 Implémenter la fonctionnalité permettant de sélectionner le numéro d'une personne.
def num_personne(tab, nom, prenom):
    for i in range(len(tab)):
        if tab[i][0] == nom and tab[i][1] == prenom:
            return i
#4
def ajout_lien(tab, num1, num2):
    tab.append([num1, num2])
    return tab
#5
def ascendants(tab, num):
    ascendants = []
    for i in range(len(tab)):
        if tab[i][1] == num:
            ascendants.append(tab[i][0])
    return ascendants
#6 
def descendants(tab, num):
    descendants = []
    for i in range(len(tab)):
        if tab[i][0] == num:
            descendants.append(tab[i][1])
    return descendants
#7
def freres_soeurs(tab, num):
    freres_soeurs = []
    for i in range(len(tab)):
        if tab[i][0] == num:
            freres_soeurs.append(tab[i][1])
    return freres_soeurs
#8
def tri(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][0] < tab[j][0]:
                tab[i], tab[j] = tab[j], tab[i]
            elif tab[i][0] == tab[j][0]:
                if tab[i][1] < tab[j][1]:
                    tab[i], tab[j] = tab[j], tab[i]
    return tab
#9 
def tri_age(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][3][2] < tab[j][3][2]:
                tab[i], tab[j] = tab[j], tab[i]
            elif tab[i][3][2] == tab[j][3][2]:
                if tab[i][3][1] < tab[j][3][1]:
                    tab[i], tab[j] = tab[j], tab[i]
                elif tab[i][3][1] == tab[j][3][1]:
                    if tab[i][3][0] < tab[j][3][0]:
                        tab[i], tab[j] = tab[j], tab[i]
    return tab

ajout(les_personnes, "DUPONT", "Jean", "M", [12, 5, 1980])
ajout(les_personnes, "Yoan", "Croisier", "F", [26, 12, 2003])
ajout(les_personnes, "El Akhal", "Mohamad", "M", [12, 5, 2003])
ajout(les_personnes, "Noah", "Clergaud-Metraud", "M", [31, 6, 2010])
ajout(les_personnes, "Léa", "Clergaud-Metraud", "F", [25, 4 , 2010])

ajout_lien(lien_parente, num_personne(les_personnes, "DUPONT", "Jean"), num_personne(les_personnes, "Yoan", "Croisier"))
ajout_lien(lien_parente, num_personne(les_personnes, "DUPONT", "Jean"), num_personne(les_personnes, "El Akhal", "Mohamad"))
ajout_lien(lien_parente, num_personne(les_personnes, "Yoan", "Croisier"), num_personne(les_personnes, "El Akhal", "Mohamad"))
ajout_lien(lien_parente, num_personne(les_personnes, "El Akhal", "Mohamad"), num_personne(les_personnes, "Noah", "Clergaud-Metraud"))
ajout_lien(lien_parente, num_personne(les_personnes, "El Akhal", "Mohamad"), num_personne(les_personnes, "Léa", "Clergaud-Metraud"))
ajout_lien(lien_parente, num_personne(les_personnes, "Yoan", "Croisier"), num_personne(les_personnes, "Lea", "Clergaud-Metraud"))

print(les_personnes)
print(lien_parente)

print(descendants(lien_parente, num_personne(les_personnes, "El Akhal", "Mohamad")))