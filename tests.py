from projet_poo import *
def selection(x): 
    

    equipe = []
    print("Veuillez choisir vos creatures pour le combat.")
 

    for i, p in enumerate(x): 
        print(f"{i + 1}: {p}") 
 
    while len(equipe) < 2: 
        choix = input("Choisissez une creature (1-3): ")

        if choix.isdigit() and 1 <= int(choix) <= 3: 
            choix = int(choix) - 1 
            if x[choix] not in equipe:
                equipe.append(x[choix]) 
                print(f"{x[choix].nom} a été ajouté à votre équipe.") 
            else: 
                print("déjà été choisi, choisissez autrement.") 
        else: 
            print("Choix invalide, veuillez entrer un nombre entre 1 et 3.") 
    print("Vos creatures sont prêtes!")
 
    return equipe
