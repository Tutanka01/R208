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
#6 Idem mais pour les descendants d'une personne cette fois.
def descendants(tab, num):
    descendants = []
    for i in range(len(tab)):
        if tab[i][0] == num:
            descendants.append(tab[i][1])
    return descendants

#7 Idem pour les frères et soeurs d'une personne donnée.

def freres_soeurs(tab, num):
    freres_soeurs = []
    pere = []
    errors = ""
    print(len(tab))
    for i in range(len(tab)):
        if tab[i][1] == num:
            print(tab[i][1])
            pere.append(tab[i][0])

    for i in range(len(tab)):
        if tab[i][0] == pere[0]:
            freres_soeurs.append(tab[i][1])
    
    for i in range(len(freres_soeurs)):
        if freres_soeurs[i] == num:
            freres_soeurs.pop(i)
    return freres_soeurs
    
#8
def tri(tab):
    for i in range(len(tab)): #Pour chaque personne de la liste
        for j in range(len(tab)): #On compare la personne à toutes les autres personnes de la liste
            if tab[i][0] < tab[j][0]: #Si le nom de la personne i est avant le nom de la personne j
                tab[i], tab[j] = tab[j], tab[i] #On inverse les deux personnes
            elif tab[i][0] == tab[j][0]: #Si les noms sont les mêmes
                if tab[i][1] < tab[j][1]: #On compare les prénoms
                    tab[i], tab[j] = tab[j], tab[i] #On inverse les deux personnes
    les_personnes = tab
    return affichage(les_personnes)
#9 
'''Dans cette fonction on va comparer les années de naissance des personnes, puis les mois et enfin les jours.
pour cela on va utiliser les indices 2, 1 et 0 de la liste date, on va consulter une par une les dates de chaque 
personne pour voir qui a le jour le moins eleve, puis le mois le moins eleve et enfin l'annee la moins elevee.'''

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
    les_personnes = tab
    return affichage(les_personnes)

def menu():
    print("1. Ajouter une personne")
    print("2. Afficher les personnes")
    print("3. Sélectionner le numéro d'une personne")
    print("4. Ajouter un lien de parenté")
    print("5. Afficher les ascendants d'une personne")
    print("6. Afficher les descendants d'une personne")
    print("7. Afficher les frères et soeurs d'une personne")
    print("8. Trier les personnes par ordre alphabétique")
    print("9. Trier les personnes par ordre d'âge")
    print("10. Quitter")
    choix = int(input("Votre choix : "))
    return choix

def main():
    while True:
        choix = menu()
        if choix == 1:
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            sexe = input("Sexe : ")
            date = input("Date de naissance : ")
            date = date.split("/")
            date = [int(date[0]), int(date[1]), int(date[2])]
            ajout(les_personnes, nom, prenom, sexe, date)
            print('\n')
            
        elif choix == 2:
            affichage(les_personnes)
        
        elif choix == 3:
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            print(num_personne(les_personnes, nom, prenom))
            print('\n')
        
        elif choix == 4:
            nom1 = input("Nom de la première personne : ")
            prenom1 = input("Prénom de la première personne : ")
            nom2 = input("Nom de la deuxième personne : ")
            prenom2 = input("Prénom de la deuxième personne : ")
            ajout_lien(lien_parente, num_personne(les_personnes, nom1, prenom1), num_personne(les_personnes, nom2, prenom2))
        
        elif choix == 5:
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            print(ascendants(lien_parente, num_personne(les_personnes, nom, prenom)))
        
        elif choix == 6:
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            print(descendants(lien_parente, num_personne(les_personnes, nom, prenom)))
       
        elif choix == 7:
            num = int(input("Numéro de la personne : "))
            print(freres_soeurs(lien_parente, num))
        
        elif choix == 8:
            print(tri(les_personnes))
        
        elif choix == 9:
            print(tri_age(les_personnes))
        
        elif choix == 10:
            break
        
        else:
            print("Erreur de saisie")



ajout(les_personnes, "DUPONT", "Jean", "M", [12, 5, 1980])
ajout(les_personnes, "Sophie", "Metatidj", "F", [26, 12, 2003])
ajout(les_personnes, "El Akhal", "Mohamad", "M", [12, 5, 2003])
ajout(les_personnes, "Noah", "Clergaud-Metraud", "M", [31, 6, 2010])
ajout(les_personnes, "Léa", "Clergaud-Metraud", "F", [25, 4 , 2010])
ajout(les_personnes, "Wafa", "Bhamza", "F", [26, 4 , 2010])
ajout(les_personnes, "lucas", "modric", "F", [27, 4 , 2010])

ajout_lien(lien_parente, num_personne(les_personnes, "DUPONT", "Jean"), num_personne(les_personnes, "Sophie", "Metatidj"))
ajout_lien(lien_parente, num_personne(les_personnes, "DUPONT", "Jean"), num_personne(les_personnes, "El Akhal", "Mohamad"))
ajout_lien(lien_parente, num_personne(les_personnes, "Sophie", "Metatidj"), num_personne(les_personnes, "El Akhal", "Mohamad"))
ajout_lien(lien_parente, num_personne(les_personnes, "El Akhal", "Mohamad"), num_personne(les_personnes, "Noah", "Clergaud-Metraud"))
ajout_lien(lien_parente, num_personne(les_personnes, "El Akhal", "Mohamad"), num_personne(les_personnes, "Léa", "Clergaud-Metraud"))
ajout_lien(lien_parente, num_personne(les_personnes, "Sophie", "Metatidj"), num_personne(les_personnes, "Léa", "Clergaud-Metraud"))
ajout_lien(lien_parente, num_personne(les_personnes, "Sophie", "Metatidj"), num_personne(les_personnes, "Wafa", "Bhamza"))
ajout_lien(lien_parente, num_personne(les_personnes, "Wafa", "Bhamza"), num_personne(les_personnes, "lucas", "modric"))
print(lien_parente)

main()