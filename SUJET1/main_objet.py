#A FINIR!!!
import sys

# On Commence lea meme que main.py mais en objet :)
# Voir main.py pour avoir les questions une par une, flemme de les recopier :)

class donnee():
    def __init__(self, id_capteur = int, date = [], heure = [], type=str, valeur=float):
        # Donnes qui appartiennent strictemment a l'objet lui meme
        self.id_capteur = id_capteur
        self.date = date
        self.heure = heure
        self.type = type
        self.valeur = valeur
        self.data = {}
        # Partie de gestion d'erreur
        self.errors = ""
        
    def ajout(self):
        self.data[self.id_capteur] = [self.date, self.heure, self.type, self.valeur]
        # verification de la date format max [31, 12, 2099] -> [jour,mois, annee]
        if self.data[self.id_capteur][0][0] > 31 or self.data[self.id_capteur][0][1] > 12 or self.data[self.id_capteur][0][2] > 2099:
            self.errors += "la date n'esst pas bonne pour la ligne {}".format(self.data) + "\n"
        # verification de l'heure format max [23,59,59] -> [heure(24h),min,sec]
        if self.data[self.id_capteur][1][0] >= 24 or self.data[self.id_capteur][1][1] >= 60 or self.data[self.id_capteur][1][2] >= 60:
            self.errors += "L'heure n'est pas dans le bon format pour la ligne {}".format(self.data) + "\n"
        # si la variable self.errors n'est pas vide arreter le programme et returner l'erreur
        if self.errors != "":
            sys.exit(self.errors)
        return self.date
    
    def affichage(self):
        for i in range(len(self.data[self.id_capteur])):
            print("La valeur d'indice {} est :".format(i), self.data[self.id_capteur][i])    
    
    # Pour le filtrage je me suis dit que dans aucun cas il y aura 2 id differents dans le meme objet
    # car chaqu'un d'eux est un objet, on peut faire plus simple, je sais,  mais flemme :)
    def filtrage_id(self,id_capteur=int):
        if id_capteur != self.id_capteur:
            self.errors += "Votre id est invalide"
            sys.exit(self.errors)
        else:
            return self.data[id_capteur]
    # Ici je me suis dit la meme chose, a corriger si faux
    def filtrage_date(self, date = list):
        if date not in self.data[self.id_capteur]:
            self.errors += "Votre date est invalide"   
            sys.exit(self.errors)
        else:
            return self.data[self.id_capteur]
    
donne1 = donnee(1248,[14,5,2012],[12,30,55],  "température", 25.5)
donne2 = donnee(1249,[15,5,2012],[12,35,55],  "température", 27.5)


donne1.ajout()
donne2.ajout()

print(donne2.affichage())