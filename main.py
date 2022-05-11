from typing import TYPE_CHECKING
from os import system
import time

def clear():
    _ = system('cls')

everythinkok = False
need = 5
mdp=input(f"Mot de passe (> {need} caractères): ")
longueur = len(mdp)
while longueur < need:
    print(f"{need} caractères nécessaires, merci de réessayer")
    mdp=input(f"Mot de passe ({need} caractères): ")
    longueur = len(mdp)
if longueur >= need:
    print(mdp)
    verif=input("Entrez votre mot de passe: ")
    print(verif)
    while mdp != verif:
        print("Mot de passe incorrect, merci de réessayer ")
        verif=input("Entrez votre mot de passe: ")
    if mdp == verif:
        nom=input("Nom ? ")
        prenom=input("Prénom ? ")
        age=input("Age ? ")
        while not nom or not prenom or not age:
            print("Merci d'entrer quelque chose dans chaques catégories.")
            nom=input("Nom ? ")
            prenom=input("Prénom ? ")
            age=input("Age ? ")
        print(nom, prenom, age, "ans")
        time.sleep(3)
        newMdp = input("Entrez un nouveau mot de passe pour accédez quand vous voulez à vos informations personnelles: ")
        newMdpL = len(newMdp)
        sécurité = "Mauvaise"
        sécuritémdp1 = "Mauvaise"
        while newMdp == mdp or newMdpL < need:
            if newMdpL < need:
                print(f"Votre mot de passe ne contient pas suffisamment de caractères ({newMdpL} sur {need}), merci de réessayer: ")
                newMdp = input()
                newMdpL = len(newMdp)
            else:
                print("Votre mot de passe a déjà été utilisé précédemment, merci de réessayer: ")
                newMdp = input()
                newMdpL = len(newMdp)
            #print(f"Votre mot de passe à déjà été utilisé précédemment ou ne contient pas suffisamment de caractères ({newMdpL} sur {need}), merci de réessayer: ")
            #newMdp = input()
            #newMdpL = len(newMdp)
        if newMdp != mdp and newMdpL >= need:
            if newMdpL > 5:
                sécurité = "correcte"
            if newMdpL > 7:
                sécurité = "Bonne"
            if newMdpL > 9:
                sécurité = "Excellente"
            if longueur > 5:
                sécuritémdp1 = "correcte"
            if longueur > 7:
                sécuritémdp1 = "Bonne"
            if longueur > 9:
                sécuritémdp1 = "Excellente"
            print("Votre mot de passe a été accepter, entrez 'mdp' si vous souhaitez consulter votre mot de passe ou 'infos' si vous souhaitez accéder à vos informations")
            var = input()
            while var != 'infos':
                if var == 'mdp':
                    break
                print("Entrez 'mdp' ou 'infos': ")
                var = input()
            if var == 'mdp':
                print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                var = input()
                while var != 'close':
                    clear()
                    if var == 'close':
                        print("Closed")
                        break
                    else:
                        if var == 'infos':
                            print(nom, prenom, age, "ans")
                            print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                            var = input()
                            if var == 'infos':
                                print(nom, prenom, age, "ans")
                                print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                var = input()
                            else:
                                if var != 'close':
                                    if var == 'mdp':
                                        print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                        print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                        var = input()
                                    else:
                                        if var == 'infos':
                                            print(nom, prenom, age, "ans")
                                            print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                            var = input()
                                else:
                                    print("Closed")
                            #else:
                                #if var == 'mdp':
                                 #   print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                  #  print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                   # var = input()
                                #else:
                                   # if var == 'close':
                                    #    break
                                #if var == 'mdp':
                                 #   print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                  #  print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                   # var = input()
                                #else:
                                   # print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                        else:
                            if var == 'mdp':
                                print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                var = input()
                            else:
                                while var != 'infos':
                                    if var != 'mdp':
                                        print("Entrez 'mdp' ou 'infos': ")
                                        var = input()
                                    else:
                                        break
                                if var != 'close':
                                    if var == 'mdp':
                                        print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                        print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                        var = input()
                                    else:
                                        if var == 'infos':
                                            print(nom, prenom, age, "ans")
                                            print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                            var = input()
                                else:
                                    print("Closed")

            if var == 'infos':
                print(nom, prenom, age, "ans")
                print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                var = input()
                while var != 'close':
                    clear()
                    if var == 'close':
                        print("Closed")
                        break
                    else:
                        if var == 'infos':
                            print(nom, prenom, age, "ans")
                            print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                            var = input()
                            if var == 'infos':
                                print(nom, prenom, age, "ans")
                                print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                var = input()
                            else:
                                if var != 'close':
                                    if var == 'mdp':
                                        print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                        print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                        var = input()
                                    else:
                                        if var == 'infos':
                                            print(nom, prenom, age, "ans")
                                            print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                            var = input()
                                else:
                                    print("Closed")
                            #else:
                                #if var == 'mdp':
                                 #   print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                  #  print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                   # var = input()
                                #else:
                                   # if var == 'close':
                                    #    break
                                #if var == 'mdp':
                                 #   print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                  #  print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                   # var = input()
                                #else:
                                   # print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                        else:
                            while var != 'infos':
                                if var != 'mdp':
                                    print("Entrez 'mdp' ou 'infos': ")
                                    var = input()
                                else:
                                    break
                            if var == 'mdp':
                                print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                var = input()
                            else:
                                if var != 'close':
                                    if var == 'mdp':
                                        print(f"Votre premier mot de passe est: {mdp} il contient {longueur} caractères et possède donc une sécurité classée: {sécurité} . Votre second mot de passe est: {newMdp}, il contient {newMdpL} caractères et possède donc une sécurité classée: {sécurité} ")
                                        print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                        var = input()
                                    else:
                                        if var == 'infos':
                                            print(nom, prenom, age, "ans")
                                            print("Entrez 'infos' pour accéder à vos informations, 'mdp' pour accéder aux informations de votre mot de passe et 'close' pour fermer la fenêtre:")
                                            var = input()
                                else:
                                    print("Closed")
        else:
            print("Il y a un problème")
    else:
        print("Mot de passe incorrect ")