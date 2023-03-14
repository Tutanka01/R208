import sys

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

date3 = [27,2,2024] # en format jour/mois/année
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

def cles():
    #Append all the keys of a dico that is in a list in a list
    cles_liste = []
    for i in range(0, len(data)):
        cles_liste.append(list(data[i].keys()))
    return cles_liste

def 
   
def ajout(id_capteur,date, heure, type_capteur, valeur):
    errors = ""
    dico_temp = {}
    dico_temp[str(id_capteur)] = [date, heure, type_capteur, valeur]
    
    # verifier si la date est dans le bon format
    if dico_temp[str(id_capteur)][0][0] > 31 or dico_temp[str(id_capteur)][0][1] > 12 or dico_temp[str(id_capteur)][0][2] > 2099:
        errors += "La date n'est pas dans le bon format" + '\n'
    # verifier si l'heure est dans le bon format
    if dico_temp[str(id_capteur)][1][0] > 60 or dico_temp[str(id_capteur)][1][1] > 60 or dico_temp[str(id_capteur)][1][2] > 60:
        errors += "L'heure n'est pas dans le bon format" + '\n'
    # Il verifie si erros est vide, si oui, il ne fait rien, sinon, il quitte le programme et retourne toutes les ereurs
    if errors == "":
        pass
    else:
        sys.exit(errors)
    
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
    

"""Implémenter la fonctionnalité permettant de filtrer un tableau de stockage pour ne conserver que les
lignes concernant un capteur donné. Cette fonction prendra en entrée (aka en paramètre) un tableau
de stockage ainsi que l'identifiant du capteur, et retournera comme résultat un nouveau tableau de
stockage (même "format") contenant uniquement les lignes retenues."""

def filtrage_id(id_capteur):
    data_temp = []
    cles_liste = cles()
    for i in range(len(data)):
        if id_capteur == int(cles_liste[i][0]):
            data_temp.append(data[i])
    return data_temp

"""Idem pour un intervalle de temps donné (entre telle date telle heure et telle date telle heure), pour
un type de capteur donné, etc. . . Le fait que ces fonctions de sélection fonctionnent à la manière de
filtres, c'est-à-dire qu'elles prennent en entrée un tableau de stockage et un critère pour retourner en
sortie un tableau de stockage, va nous permettre "d'emboîter" ces filtres pour réaliser des recherches
multi-critères."""
# A finir
def filtrage_date(date):
    data_temp = []
    cles_liste = cles()
    for i in range(len(data)):
        if date == data[i][cles_liste[i][0]][0]:
            data_temp.append(data[i])    
    return data_temp

def str_liste(type): # Cette fonction permet de créer une liste à partir d'entrées de l'utilisateur
    lst=[]
    if type == "date":
        for i in range(0,3):
            ele = int(input())
            lst.append(ele)
    elif type == "heure":
        for i in range(0,3):
            ele = int(input())
            lst.append(ele)
    return(lst)
# valeur minimum/maximum/moyenne d'un capteur sur la totalité des données collectées (il y a
# donc 3 fonctions à écrire)

def min_val():
    try:
        lst_keys = cles()
        min_val = data[0][lst_keys[0][0]][3]
        for i in range(0, len(data)):
            if data[i][lst_keys[i][0]][3] < min_val:
                min_val = data[i][lst_keys[i][0]][3]
        return min_val
    except:
        return 0
def max_val():
    lst_keys = cles()
    min_val = data[0][lst_keys[0][0]][3]
    for i in range(0, len(data)):
        if data[i][lst_keys[i][0]][3] > min_val:
            min_val = data[i][lst_keys[i][0]][3]
    return min_val
def moy_val():
    lst_keys = cles()
    somme = 0
    for i in range(len(data)):
        try:
            somme += data[i][lst_keys[i][0]][3]
        except IndexError:
            print("L'index n'existe pas")
        except KeyError:
            print("La clé n'existe pas")
    moy = somme / len(data)
    return moy.__round__(2)
    
def main():
    print("Bienvenue dans le programme de gestion des données de capteurs")
    print("1. Ajouter une nouvelle valeur")
    print("2. Afficher toutes les données collectées")
    print("3. Filtrer les données par capteur")
    print("4. Filtrer les données par date")
    choix = int(input("Que voulez-vous faire ? "))
    if choix == 1:
        id_capteur = int(input("Entrez l'identifiant du capteur : "))
        print("Entrez la date (format jj/mm/aaaa) en forme de tableau : ")
        date = str_liste('date')
        print("Entrez l'heure (format hh/mm/ss) en forme de tableau : ")
        heure = str_liste('heure')
        type_capteur = input("Entrez le type de capteur : ")
        valeur = float(input("Entrez la valeur relevée par le capteur : "))
        ajout(id_capteur, date, heure, type_capteur, valeur)
    elif choix == 2:
        print(data)
    elif choix == 3:
        print("Entrez l'identifiant du capteur que vous voulez filtrer : ")
        capteur = int(input())
        print(filtrage_id(capteur))
    elif choix == 4:
        print("Entrez la date que vous voulez filtrer (format jj/mm/aaaa) une valeur apres l'autre:  \n")
        date_filtre = str_liste('date')
        print(filtrage_date(date_filtre)) 
    else:
        print("c'est faux mon reuf , tu dois choisir entre 1 et 4")
        
ajout(id_capteur, date, heure, type_capteur, valeur)
ajout(id_capteur2, date2, heure2, type_capteur2, valeur2)
ajout(id_capteur3, date3, heure3, type_capteur3, valeur3)
main()