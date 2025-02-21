from random import randint
import time
from tests import *

#import keyboard  # on importe le module keyboard

# Variables a definir :
typedegats = {"Contondant": 5, "Tranchant": 10, "Percant": 20, "Feu": 25, "Poison": 30, "Magique": 30}
etat = {"empoisonne", "paralyse", "inspire"}
armes = {"claymore", "katana", "THESE HANDS", "special ability"}

# Fonction pour simuler un lancer de de
def de(n):
    return randint(1, n)
def trier(personnages):
    for personnage in personnages:
        personnage.de = de(20)
        print(f"{personnage.nom} a lancé un {personnage.de}")
    personnages.sort(key=lambda x: x.de, reverse=True)
    return personnages

def afficher_les_messages_lentement(message, vitesse=0.01):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(vitesse) 
# le debut du code combat et..j'ai oublie xD  ta oublier quoi ??
def intro():
    afficher_les_messages_lentement("Bienvenue dans D&D, appuyez sur 'Entree' pour continuer.")
    yippie = input()
    #keyboard.wait('enter')  # Attendre la touche "Entree"
    
    afficher_les_messages_lentement(f"Veuillez choisir votre personnage. \n")

    global hero, monstre

    combat()

class Creature:
    def __init__(self, nom, desc, typedegats, degats,pv, etat,de):
        self.nom = nom
        self.desc = desc
        self.typedegats = typedegats
        self.degats = degats
        self.pv = pv
        self.etat = etat
        self.de = de
    def isdead(self) :
        return self.pv <= 0
    def attaque(self, cible):
        n = de(20)
        if n > cible.defense :
            cible.pv -= int(self.degats)
            print(f"{self.nom} attaque {cible.nom} et inflige {self.degats} degats!")
        else : 
            print("AWh, l'attaque a echoue!")

    # fonctions buff/debuff :
    def buff(self,n) :
        self.degats = self.degats * n # n est un multiplicateur de dégats

    def debuff(self,cible,n) :
        cible.degats = cible.degats / n # n : diviseur de dégats 


class Personnage(Creature):
    def __init__(self, nom, desc, pv,typedegats, degats, etat, arme,de):
        super().__init__(nom, desc, pv, typedegats, degats, etat,de)
        self.arme = arme

    def __str__(self):
        return f"Nom: {self.nom}, Desc: {self.desc}, Type: {self.typedegats}, Degats: {self.degats}, Arme: {self.arme}"

    def volpv(self, cible):
        soin = randint(5, 10)
        print(f"{self.nom} recupere {soin} PV en volant la vie de {cible.nom}.")
        self.pv += soin
        cible.pv -= soin
    def htpurple(self,cible) :
        print("Hollow technique : Purple.")
        print(f"{self.nom} utilise sa capacite speciale sur {cible.nom}, bro is cooked.")
        cible.pv -= 60
    def bankai(self,cible) :
        print("Bankai !")
        
        print(f"{self.nom} utilise sa capacite speciale sur {cible.nom}, bro is BEYOND cooked.")
        print("multiple slashes later...")
        cible.pv -= 100




class Monstre(Creature):
    def __init__(self, nom, description, pv, typedegats,defense, degats, etat,resistance,de):
        super().__init__(nom, description, pv,typedegats, degats,etat,de)
        self.resistance = resistance
        self.defense = defense
    def __str__(self):
        return f"Nom: {self.nom}, Desc: {self.desc}, Type: {self.typedegats}, Degats: {self.degats}, Resistance :{self.resistance}"

    def atkmonstre(self, cible):
        degats = randint(1, self.degats)
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} degats!")
        cible.pv -= degats
    def dabiflame(self, cible) :
        degats = randint(1,self.degats)*3
        print(f"{self.nom} attaque continuously {cible.nom} et inflige {degats} degats!")
        cible.pv -= degats 
        cible.etat = "Burning"
        print(f"oh no ! {cible.nom} is burning, too bad.")
                    



def combat():
    global hero, monstre

    listep = [
        Personnage("Gojo Satoru", "top tier sorcerer", "Magique",30, 150, "", "THESE HANDS",0),
        Personnage("Dazai Osamu", "a suicidal genius", "Magique",30, 150, "", "special ability",0),
        Personnage("Kurosaki Ichigo", "Un Shinigami", "Percant", 20,150, "", "katana",0)
    ]
    listem = [
        Monstre("Goblin", "ugly fugly creature", "Contendant",5,10,100,  "", "Feu",0),
        Monstre("Ruin Guard", "Automated robot built ", "Percant",20,10,100,  "", "rien",0),
        Monstre("Dabi", "Supervillain with high flame power", "Feu",25,5,100,  "", "Feu",0)
    ]

    listep = selection(listep)  
    listem = selection(listem)  

    # Sélection du héros
    while True:
        for i, p in enumerate(listep):
            print(f"{i + 1}: {p.nom}")
        choix = input("Choisissez un personnage (1-3): ")
        if choix.isdigit() and 1 <= int(choix) <= len(listep):
            hero = listep[int(choix) - 1]
            break
        else:
            print("Choix invalide ! Veuillez entrer un nombre entre 1 et 3.")

    # Sélection du monstre
    while True:
        for i, m in enumerate(listem):
            print(f"{i + 1}: {m.nom}")
        choixx = input("Choisissez un monstre (1-3): ")
        if choixx.isdigit() and 1 <= int(choixx) <= len(listem):
            monstre = listem[int(choixx) - 1]
            break
        else:
            print("Choix invalide ! Veuillez entrer un nombre entre 1 et 3.")

    # Création et tri de la liste des combattants
    listefinale = listep + listem
    listefinale = trier(listefinale)

    print("\n FIGHT! :")
    for combattant in listefinale:
        print(f"- {combattant.nom} ({combattant.pv} PV)")

    # Boucle principale du combat
    while True:
        for combattant in listefinale:
            if combattant.isdead():
                continue  

            print(f"\n C'est au tour de {combattant.nom} d'attaquer !")

            # Déterminer la cible (si c'est un personnage, attaque un monstre, et vice versa)
            cibles = listem if isinstance(combattant, Personnage) else listep
            cibles = [c for c in cibles if not c.isdead()]  

            if not cibles:  
                continue
            while True:
                a = input("choisissez votre cible : 1 ou 2 :")
                if a == '1' and not cibles[0].isdead():
                    cible = cibles[0]
                    break
                elif a == '2' and not cibles[1].isdead():
                    cible = cibles[1]
                    break
                else: 
                    print("choix invalide, veuillez choisir 1 ou 2.")
                   
                
            
            if isinstance(combattant, Personnage):
                while True:
                    methode = input(f"{combattant.nom}! Choisis ta méthode d'attaque : 1-Normal 2-Spécial 3-Buff 4-Debuff l'ennemi : ")
                    if methode == '1':
                        combattant.attaque(cible)
                        break
                    elif methode == '2':
                        if combattant.nom == "Gojo Satoru": 
                            combattant.htpurple(cible)
                        elif combattant.nom == "Dazai Osamu": 
                            combattant.volpv(cible)
                        else:
                            combattant.bankai(cible)
                        break
                    elif methode == '3':
                        multiplier = de(3)
                        decidor = randint(0,10)
                        if decidor > 3:
                            combattant.buff(multiplier)
                            print(f"{combattant.nom} a buff ses degats de {multiplier}!")
                        else: 
                            print("le buff a echoue.")
                        break
                    elif methode == '4':
                        dividor = de(3)
                        decidor = randint(0,10)
                        if decidor > 3:
                            combattant.debuff(cible,dividor)
                            print(f"{combattant.nom} a debuff les degats de {cible.nom} de {dividor}!")
                        else: 
                            print("le debuff a echoue.")
                        break
                    else:
                        print("Choix invalide ! Veuillez entrer 1, 2, 3 ou 4.") 

            
            elif isinstance(combattant, Monstre):
                while True:
                    methode = input(f"{combattant.nom}! Choisis ta méthode d'attaque : 1-Normal 2-Spécial (ONLY DABI) 3-Buff 4-Debuff l'ennemi : ")
                    if methode == '1':
                        combattant.atkmonstre(cible)
                        break
                    elif methode == '2' and combattant.nom == "Dabi":
                        combattant.dabiflame(cible)
                        break
                    elif methode == '3':
                        multiplier = de(2)
                        decidor = randint(0,10)
                        if decidor > 3:
                            combattant.buff(multiplier)
                            print(f"{combattant.nom} a buff ses degats de {multiplier}!")
                        else: 
                            print("le buff a echoue.")
                        break
                    elif methode == '4':
                        dividor = de(4)
                        decidor = randint(0,10)
                        if decidor > 3:
                            combattant.debuff(cible,dividor)
                            print(f"{combattant.nom} a debuff les degats de {cible.nom} de {dividor}!")
                        else: 
                            print("le debuff a echoue.")
                        break
                    else:
                        print("Choix invalide ! Veuillez entrer 1, 2 (seul Dabi peut utiliser 2), 3 ou 4.")

            # Afficher les PV après chaque attaque
            print(f"{combattant.nom} a {combattant.pv} PV !")
            print(f"{cible.nom} a {cible.pv} PV !")

            
            if all(m.isdead() for m in listem):  
                print("\nFélicitations, vous avez vaincu tous les monstres !")
                return
            if all(p.isdead() for p in listep):
                print("\nDéfaite... Tous les héros sont morts.")
                return


if __name__ == "__main__":
    intro()
    print("Fin du jeu.")


# def choix_armes():
    # listam = ["objets maudit","annulation d'attaque","Sabre","Katana"]
    # for i, arme in enumerate (listam, 1)
    # print(f"{i}.{arme}")

#     print("choissez une arme : {listam}")
#while true :
 #   choix = input("veuillez choisir une arme   ")
#  print ()

    