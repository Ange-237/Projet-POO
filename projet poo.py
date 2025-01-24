from random import randint
import time
import keyboard # on importe le module keyboard

#variables a definir :
typedegats ={"Contondant" :5, "Tranchant" :10, "Percant" :20, "Feu":25, "Poison":30, "Magique":30}
etat ={"empoisonné","paralysé","inspiré"}
# verif sert a verifier que le nombre est dans l'intervalle.
def verif(n):
    while True:
        if n.isdecimal():
            n_int = int(n)
            if n_int in {4, 6, 8, 10, 12, 20, 100}:
                return n_int
        print("Choix incorrect ! Essayez à nouveau :")
        n = input("Donner le type de dé (4, 6, 8, 10, 12, 20, 100 faces) >> ")
# juste fait tourner le dé lolololol
def de(n):
    return randint(1, n)
#code d'ivonne :
def afficher_les_messages_lentement(message,vitesse = 0.06) :

    for char in message:
        print(char, end="", flush=True)
        time.sleep(vitesse)



def message_de_bienvenue():

    afficher_les_messages_lentement("Bienvenue dans D&D, appuyez sur 'Entrée' pour continuer.")

    while True:
        
        if keyboard.read_key() == "enter":  # Attendre la touche "Entrée"
            print()
            afficher_les_messages_lentement(f"Veuillez choisir votre personnage.")
            break  # Sortir de la boucle après avoir pressé 'Entrée'

message_de_bienvenue() 



class Creature() :
    nom =""
    desc =""
    typedegats =""
    degats = 0
    pv = 150
    etat =""

    def __init__(self, nom,desc,typedegats,degats,etat):
        self.nom = nom
        self.desc=desc
        self.typedegats = typedegats
        self.degats = degats
        self.etat=etat
    

    def attaque(self, cible):
        # Ici les concéquences de l'attaque
        cible.pv = cible.pv - self.degats
         # A supprimer quand la fonction sera écrite

    class Personnage(Creature):
        def  __init__(self,arme) :
            self.arme = arme
    


#petits tests pour s'assurer que ça focntionne 
gojo = Personnage("Gojo Satoru","top tier sorcerer","Magique",)
n = input("Donner le type de dé (4, 6, 8, 10, 12, 20, 100 faces) >> ")
n = verif(n)
r = de(n)
print("Votre nombre est :", r)


    