from random import randint
import time
import keyboard  # on importe le module keyboard

# Variables a definir :
typedegats = {"Contondant": 5, "Tranchant": 10, "Percant": 20, "Feu": 25, "Poison": 30, "Magique": 30}
etat = {"empoisonne", "paralyse", "inspire"}
armes = {"claymore", "katana", "THESE HANDS", "special ability"}

# Fonction pour simuler un lancer de de
def de(n):
    return randint(1, n)

def afficher_les_messages_lentement(message, vitesse=0.01):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(vitesse)

def intro():
    afficher_les_messages_lentement("Bienvenue dans D&D, appuyez sur 'Entree' pour continuer.")
    yippie = input()
    #keyboard.wait('enter')  # Attendre la touche "Entree"
    
    afficher_les_messages_lentement(f"Veuillez choisir votre personnage. \n")

    global hero, monstre

    combat()

class Creature:
    def __init__(self, nom, desc, typedegats, degats,pv, etat):
        self.nom = nom
        self.desc = desc
        self.typedegats = typedegats
        self.degats = degats
        self.pv = pv
        self.etat = etat
    def isdead(self) :
        return self.pv <= 0
    def attaque(self, cible):
        n = de(20)
        if n > cible.defense :
            cible.pv -= int(self.degats)
            print(f"{self.nom} attaque {cible.nom} et inflige {self.degats} degats!")
        else : 
            print("AWh, l'attaque a echoue!")

class Personnage(Creature):
    def __init__(self, nom, desc, pv,typedegats, degats, etat, arme):
        super().__init__(nom, desc, pv, typedegats, degats, etat)
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
    def __init__(self, nom, description, pv, typedegats,defense, degats, etat,resistance):
        super().__init__(nom, description, pv,typedegats, degats,etat)
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
        Personnage("Gojo Satoru", "top tier sorcerer", "Magique",30, 150, "", "THESE HANDS"),
        Personnage("Dazai Osamu", "a suicidal genius", "Magique",30, 150, "", "special ability"),
        Personnage("Kurosaki Ichigo", "Un Shinigami", "Percant", 20,150, "", "katana")
    ]
    listem =[ Monstre("Goblin", "ugly fugly creature", "Contendant",5,10,100,  "", "Feu"),
          Monstre("Ruin Guard", "Automated robot built ", "Percant",20,10,100,  "", "rien"),
          Monstre("Dabi", "Supervillain with high flame power", "Feu",25,5,100,  "", "Feu")
    ]
    while True:
        
        for i, p in enumerate(listep):
            print(f"{i + 1}: {p}")
        while True:
            
            choix = input("Choisissez un personnage (1-3): ").strip()
            if choix.isdigit() and 1 <= int(choix) <= 3:
                choix = int(choix) - 1
                break
            else:
                print("Veuillez entrer un nombre entre 1 et 3.")
        hero = listep[choix]

        for i, p in enumerate(listem):
            print(f"{i + 1}: {p}")
        while True:
            choixx = input("Choisissez monstre (1-3): ").strip()
            if choixx.isdigit() and 1 <= int(choixx) <= 3:
                choixx = int(choixx) - 1
                break
            else:
                print("Veuillez entrer un nombre entre 1 et 3.")
        monstre = listem[choixx]
        methodehero = input(f"{hero.nom}! Choisis ta methode d'attaque : 1-Normal 2-Special : ")
        if str(methodehero) =='1' :
            hero.attaque(monstre)
            print("")
        elif str(methodehero) =='2':
            if choix == 0 :
                hero.htpurple(monstre)
            elif choix == 1 :
                hero.volpv(monstre)
            else :
                hero.bankai(monstre)
        print(f"{hero.nom} a {hero.pv} PV ! et {monstre.nom} a {monstre.pv} PV !")
        methodemon = input(f"{monstre.nom}! Choisis ta methode d'attaque : 1-Normal 2-Special (ONLY DABI) : ")
        if str(methodemon) =='1' :
            monstre.atkmonstre(hero)
            print("")
        elif str(methodemon) =='2' and choixx == 2 :
            monstre.dabiflame(hero)
        else : 
            print("choix invalide, l'attaque special est que pour Dabi.")
            methodemon = input(f"{monstre.nom}! Choisis ta methode d'attaque : 1-Normal 2-Special (ONLY DABI) : ")    
        
        if Creature.isdead(listem[0]) and Creature.isdead(listem[1]) and Creature.isdead(listem[2]):
            print("F\u00e9licitations, vous avez gagne!")
            return
        
        if Creature.isdead(listep[0]) and Creature.isdead(listep[1]) and Creature.isdead(listep[2]):
            print("Defaite... Le monstre vous a vaincu.")
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

    