# import time
# import keyboard # on importe le module keyboard

# def afficher_les_messages_lentement(message,vitesse = 0.06) :

#     for char in message:
#         print(char, end="", flush=True)
#         time.sleep(vitesse)



# def message_de_bienvenue():

#     afficher_les_messages_lentement("Bienvenue dans D&D, appuyez sur 'Entrée' pour continuer.")

#     while True:
        
#         if keyboard.read_key() == "enter":  # Attendre la touche "Entrée"
#             print()
#             afficher_les_messages_lentement("combein de hero votn combattre ")
#             afficher_les_messages_lentement("Veuillez choisir votre personnage.")
#             
#             break  # Sortir de la boucle après avoir pressé 'Entrée'

# message_de_bienvenue() 







class creature :#creation de la classe creature 
     type_de_degat = ["contontdant","trachat","percant","Feu","poison","magique"]
     etat = ["empoisonne","paralyse","inspiré"]
     arme = ["lame maudite","katana","sabre","zanpakto"]

#attributs
def __init__(self,name,descriptiton,pv,defense,initiative,attaque,type_de_degat,etat) :

        self.name = name
        self.description = descriptiton
        self.pv = pv
        self.defense = defense
        self.initiative = initiative
        self.type_de_degat = type_de_degat
        self.etat = etat
        self.degat = attaque
    # def lancer_linitiative() : 

    # def afficher_leurs_actions() :
def afficher_leurs_caracteristiques(self) :
    print(f"[{self.name},{self.description},{self.pv},{self.initiative},{self.defense},{self.etat}]")


class personnage(creature): #classe personnage ou heros
 arme = ""
inventaire = ""
    # attributs
def __init__(self,name,descriptiton,pv,defense,initiative,attaque,type_de_degat,etat,arme,inventaire) :
    super().__init__(name,descriptiton,pv,defense,initiative,attaque,type_de_degat,etat)
    self.arme = arme
    self.inventaire = inventaire
def afficher_les_caracteristiques(self) : 
    
    return f" Nom : {self.name} ,desc : {self.description}, pv : {self.pv},,inv : {self.inventaire}"

def liste_des_personnage(personnage = {}) :
    
    personnage = {"1.gojo","2.racnar","3.tanjiro","4.ichigo"}

# gojo = personnage("artefact","lunette,sucette,portefeuille",)
# racnar = personnage("épée","boussole,vin,remède")
# tanjiro = personnage("katana,nezuko,boulette de riz")
# ichigo = personnage("zanpakto","")


class monstre(creature) : #classe monnstre 
#attribut en plus 
    def __init__ (self,resistance=[]) :
        
        self.resistance = resistance
    
def choix_armes():
    listam = ["lame maudite", "annulation d'attaque", "sabre", "katana"]
    print("Veuillez choisir une arme parmi :")
    for i, arme in enumerate(listam,1):  # Affiche la liste avec les indices commencant par un 
        print(f"{i}. {arme}")

    while True:
        try:
            choix = int(input("Entrez le numéro de l'arme : "))
            if 1 <= choix <= len(listam):  # Vérifie que le choix est valide
                print(f"Vous avez choisi : {listam[choix - 1]}")
                break
            else:
                print("Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Appeler la fonction
# choix_armes()

def liste_cible():

    listcib = ["gojo","racnar","tanjiro","ichigo","dragon noir","lune supérieur","loki"]
    print("veuillez choisir une cible:")
    for x, cible in enumerate(listcib,1):
        print(f"{x}.{cible}")
    
    while True:
        try:
            choix = int(input("Entrez le numéro de l'arme : "))
            if 1 <= choix <= len(listcib):  # Vérifie que le choix est valide
                print(f"Vous avez choisi : {listcib[choix - 1]}")
                break
            else:
                print("Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
liste_cible()
        