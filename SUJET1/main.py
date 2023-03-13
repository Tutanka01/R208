date = [25,2,2024] # en format jour/mois/année
heure = [12,30,55] # en format heure/minute/secondes
id_capteur = 812167 # identifiant du capteur
type_capteur = "température" # type de capteur
valeur = 25.5 # valeur relevée par le capteur

date2 = [26,2,2024] # en format jour/mois/année
heure2 = [12,35,55] # en format heure/minute/secondes
id_capteur2 = 812169 # identifiant du capteur
type_capteur2 = "température" # type de capteur
valeur2 = 30 # valeur relevée par le capteur

date3 = [26,2,2024] # en format jour/mois/année
heure3 = [12,40,55] # en format heure/minute/secondes
id_capteur3 = 812169 # identifiant du capteur
type_capteur3 = "température" # type de capteur
valeur3 = 35 # valeur relevée par le capteur

data = [] # indice 0 = date, indice 1 = heure, indice 2 = id_capteur, indice 3 = type_capteur, indice 4 = valeur
"""
Implémenter la fonctionnalité permettant d'ajouter une nouvelle valeur (envoyée par un capteur).
Cette fonction prend en paramètres les différentes informations, construit la nouvelle ligne et l'ajoute
au tableau.
"""

def ajout(id_capteur,date, heure, type_capteur, valeur):
    dico_temp = {}
    dico_temp[id_capteur] = [date, heure, type_capteur, valeur]
    data.append(dico_temp)

# On insinue que la fonction ajout() est appelée à chaque fois qu'un capteur envoie une valeur
# Mais aussi que le format des données est toujours le même
""" 
Implémenter la fonctionnalité permettant d'afficher, dans l'ordre d'insertion, toutes les données collectées du tableau passé en paramètre. 
Pour simplifier, point de présentation graphique ; l'affichage se fera
de manière textuelle dans la console.
"""
def affichage():
    for i in range(0, len(data)):
        print("La valeur d'indice {} est :".format(i), data[i])
    
ajout(id_capteur,date, heure, type_capteur, valeur)
ajout(id_capteur2,date2, heure2, type_capteur2, valeur2)
ajout(id_capteur3,date3, heure3, type_capteur3, valeur3)

"""Implémenter la fonctionnalité permettant de filtrer un tableau de stockage pour ne conserver que les
lignes concernant un capteur donné. Cette fonction prendra en entrée (aka en paramètre) un tableau
de stockage ainsi que l'identifiant du capteur, et retournera comme résultat un nouveau tableau de
stockage (même "format") contenant uniquement les lignes retenues."""

def filtrage_id(id_capteur):
    data_temp = []
    for i in range(0, len(data)):
        if id_capteur in data[i]:
            data_temp.append(data[i])
    return data_temp

"""Idem pour un intervalle de temps donné (entre telle date telle heure et telle date telle heure), pour
un type de capteur donné, etc. . . Le fait que ces fonctions de sélection fonctionnent à la manière de
filtres, c'est-à-dire qu'elles prennent en entrée un tableau de stockage et un critère pour retourner en
sortie un tableau de stockage, va nous permettre "d'emboîter" ces filtres pour réaliser des recherches
multi-critères."""

def filtrage_date(date):
    data_temp = []
    for i in range(0, len(data)):
        if date in data[i]:
            data_temp.append(data[i])
    return data_temp

print(filtrage_date([26,2,2024]))