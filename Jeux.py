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
#             afficher_les_messages_lentement(f"Veuillez choisir votre personnage.")
#             break  # Sortir de la boucle après avoir pressé 'Entrée'

# message_de_bienvenue() 







class creature :#creation de la classe creature 

#attributs
    def __init__(self,name,descriptiton,pv,defense,initiative,attaque,type_de_degat=["contontdant","trachat","percant","Feu","poison","magique"],etat=["empoisonne","paralyse","inspiré"]) :

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
def __init__(self,arme,inventaire = []) :

        self.arme = arme
        self.inventaire = inventaire
def afficher_les_caracteristiques(self) : 


        print(f" {self.arme} , {self.inventaire}")

def liste_des_personnage(personnage = {}) :

    personnage = { "1.gojo","2.racnar","3.tanjiro","4.ichigo"}

gojo = personnage("artefact","lunette,sucette,portefeuille",)
racnar = personnage("épée","boussole,vin,remède")
tanjiro = personnage("katana,nezuko,boulette de riz")
ichigo = personnage("zanpakto","")


class monstre(creature) : #classe monnstre 
#attribut en plus 
    def __init__ (self,resistance=[]) :
        
        self.resistance = resistance
    
