__authors__ = "Amani Miled Azer Taboubi"
__date__ = "le 5 janvier 2019"

"""Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire ! """

from plateau import Plateau
from joueur import Joueur
import sys


class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """
    plateau = Plateau()
    joueurs = []
    joueur_courant = None
    nb_parties_nulles = 0
    tour = 1

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()  # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []  # La liste des deux joueurs (initialement une liste vide).
        # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
        # Pendant le jeu et à chaque tour d'un joueur,
        # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouer avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?

        Cette méthode doit donc utiliser la méthode saisir_nombre().
        Elle doit par la suite demander à l'utilisateur les noms des joueurs.
        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.
        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.
        Il faut utiliser entre autres ces méthodes:
            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).
            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).
            *- tour(): afin d'exécuter le tour du joueur courant.
            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.
        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant.
        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """

        self.plateau.initialiser()

        print("Bienvenue au jeu Tic Tac Toe.")
        print("---------------Menu---------------")
        print("1- Jouer avec l'ordinateur.")
        print("2- Jouter avec une autre personne.")
        print("0- Quitter.")
        print("-----------------------------------")
        print("Entrez s.v.p. un nombre entre 0 et 2:? ")

        inp = self.saisir_nombre(0, 3)

        print("******************************************")

        #jouer avec l'ordinateur
        if (int(inp) == 1):
            print("Entrez s.v.p votre nom: ? ")
            p1_name = input()
            p1_pion = self.demander_forme_pion()
            p1_type = "Personne"

            Player1 = Joueur(p1_name, p1_type, p1_pion)
            self.joueurs.append(Player1)

            #choix du pion
            if (p1_pion == "X"):
                Cpu = Joueur("Colosse", "Ordinateur", "O")
                self.joueurs.append(Cpu)
            else:
                Cpu = Joueur("Colosse", "Ordinateur", "X")
                self.joueurs.append(Cpu)

            reply = "" # variable ajouter si on veut rejouer
            self.joueur_courant = self.joueurs[0]
            firstplayer = self.joueur_courant
            while (reply.upper() != "N"):
                self.plateau.initialiser()
                print(self.plateau.__str__())
                while (self.plateau.non_plein() == True):
                    self.tour(int(inp))
                    print(self.plateau.__str__())
                    #tester a chaque tour s'il existe un gagnant
                    res1 = self.plateau.est_gagnant(self.joueurs[0].pion)
                    res2 = self.plateau.est_gagnant(self.joueurs[1].pion)
                    if ((res1 == True) or (res2 == True)):# condition impossible
                        break

                #joueur 1 gagnant
                if ((res1 == True) and (res2 == False)):
                    self.joueurs[0].nb_parties_gagnees += 1
                    print(" Partie terminée! Le joueur gagnant est: ", self.joueurs[0].nom)
                    print(" Parties gagnées par ", self.joueurs[0].nom, " : ", self.joueurs[0].nb_parties_gagnees)
                    print(" Parties gagnées par ", self.joueurs[1].nom, " : ", self.joueurs[1].nb_parties_gagnees)
                    print(" Parties Nulles : ", self.nb_parties_nulles)
                    print("Voulez-vous recommencer (O,N)? ")

                    reply = input()

                    while (reply.upper() not in ["O", "N"]):
                        print("******Valeur Incorrecte******")
                        reply = input()

                # joueur 2 gagnant
                if ((res1 == False) and (res2 == True)):
                    self.joueurs[1].nb_parties_gagnees += 1
                    print(" Partie terminée! Le joueur gagnant est: ", self.joueurs[1].nom)
                    print(" Parties gagnées par ", self.joueurs[0].nom, " : ", self.joueurs[0].nb_parties_gagnees)
                    print(" Parties gagnées par ", self.joueurs[1].nom, " : ", self.joueurs[1].nb_parties_gagnees)
                    print(" Parties Nulle : ", self.nb_parties_nulles)
                    print("Voulez-vous recommencer (O,N)? ")

                    reply = input()

                    while (reply.upper() not in ["O", "N"]):
                        print("******Valeur Incorrecte******")
                        reply = input()

                #aucun gagnant
                if ((res1 == False) and (res2 == False) and self.plateau.non_plein()==False):
                    self.nb_parties_nulles += 1
                    print(" Partie terminée! Partie est Nulle ")
                    print(" Parties gagnées par ", self.joueurs[0].nom, " : ", self.joueurs[0].nb_parties_gagnees)
                    print(" Parties gagnées par ", self.joueurs[1].nom, " : ", self.joueurs[1].nb_parties_gagnees)
                    print(" Parties Nulle : ", self.nb_parties_nulles)
                    print("Voulez-vous recommencer (O,N)? ")

                    reply = input()

                    while (reply.upper() not in ["O", "N"]):
                        print("******Valeur Incorrecte******")
                        reply = input()

                if (firstplayer == self.joueurs[0]):
                    self.joueur_courant = self.joueurs[1]
                else:
                    self.joueur_courant = self.joueurs[0]

            print(" Au Revoir ")

        #jouer avec une personne
        elif (int(inp) == 2):
            print("Entrez s.v.p votre nom: ? ")
            p1_name = input()
            p1_pion = self.demander_forme_pion()
            p1_type = "Personne"

            Player1 = Joueur(p1_name, p1_type, p1_pion)
            self.joueurs.append(Player1)

            print("Entrez s.v.p le nom de l'autre joueur : ? ")
            p2_name = input()

            if (p1_pion == "X"):
                Player2 = Joueur(p2_name, 'Personne', "O")

            else:
                Player2 = Joueur(p2_name, 'Personne', "X")

            self.joueurs.append(Player2)
            reply = "O"

            while (reply.upper() == "O"):
                self.plateau.initialiser()
                self.joueur_courant = self.joueurs[0]  # 1er personne
                print(self.plateau.__str__())
                res1 = False
                res2 = False

                while (self.plateau.non_plein() == True and res1 == False and res2 == False):
                    self.joueur_courant = self.joueurs[0]  # 1er personne
                    self.tour(int(inp))  # 1er joueur
                    print(self.plateau.__str__())  # apres le saisi
                    if (self.plateau.non_plein() == True and res1 == False):
                        self.joueur_courant = self.joueurs[1]
                        self.tour(int(inp))
                        print(self.plateau.__str__())

                    res1 = self.plateau.est_gagnant(self.joueurs[0].pion)
                    res2 = self.plateau.est_gagnant(self.joueurs[1].pion)

                if ((res1 == True) and (res2 == False)):
                    self.joueurs[0].nb_parties_gagnees += 1
                    print(" Partie terminée! Le joueur gagnant est: ", self.joueurs[0].nom)
                    print(" Parties gagnées par ", self.joueurs[0].nom, " : ", self.joueurs[0].nb_parties_gagnees)
                    print(" Parties gagnées par ", self.joueurs[1].nom, " : ", self.joueurs[1].nb_parties_gagnees)
                    print(" Parties Nulle : ", self.nb_parties_nulles)
                    print("Voulez-vous recommencer (O,N)? ")

                    reply = input()

                    while (reply.upper() not in ["O", "N"]):
                        print("******Valeur Incorrecte******")
                        reply = input()

                if ((res1 == False) and (res2 == True)):
                    self.joueurs[1].nb_parties_gagnees += 1
                    print(" Partie terminée! Le joueur gagnant est: ", self.joueurs[1].nom)
                    print(" Parties gagnées par ", self.joueurs[0].nom, " : ", self.joueurs[0].nb_parties_gagnees)
                    print(" Parties gagnées par ", self.joueurs[1].nom, " : ", self.joueurs[1].nb_parties_gagnees)
                    print(" Parties Nulle : ", self.nb_parties_nulles)
                    print("Voulez-vous recommencer (O,N)? ")

                    reply = input()

                    while (reply.upper() not in ["O", "N"]):
                        print("******Valeur Incorrecte******")
                        reply = input()

                if ((res1 == False) and (res2 == False)):
                    self.nb_parties_nulles += 1
                    print(" Partie terminée! Partie est Nulle ")
                    print(" Parties gagnées par ", self.joueurs[0].nom, " : ", self.joueurs[0].nb_parties_gagnees)
                    print(" Parties gagnées par ", self.joueurs[1].nom, " : ", self.joueurs[1].nb_parties_gagnees)
                    print(" Parties Nulle : ", self.nb_parties_nulles)
                    print("Voulez-vous recommencer (O,N)? ")

                    reply = input()

                    while (reply.upper() not in ["O", "N"]):
                        print("******Valeur Incorrecte******")
                        reply = input()

                '''if(firstplayer == self.joueurs[0]):

                    self.joueur_courant = self.joueurs[1]
                else:
                    self.joueur_courant = self.joueurs[0]'''

            print(" Au Revoiraaaaa ")
        else:
            print("Merci au Revoir")
            sys.exit(0)

    def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."

        inp = input()
        while ((inp.isnumeric() == False) or (int(inp) not in range(nb_min, nb_max))):
            print("*******Valeur Incorrecte**********")
            print("Entrez s.v.p. un nombre entre 0 et 2:? ")
            inp = input()

        return inp

    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """

        print("Entrez s.v.p la forme de votre pion ? ")
        pion = input()

        while (pion.upper() not in ['X', 'O']):
            print("******Valeur Incorrect******")
            pion = input()

        return pion.upper()

    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."

        self.plateau.__str__()
        if (choix == 1):#jourer avec ordinateur
            if (self.joueur_courant == self.joueurs[0]):
                if (self.joueur_courant.type == "Personne"):
                    ligne, colonne = self.demander_position()
                    self.plateau.selectionner_case(int(ligne), int(colonne), self.joueur_courant.pion)
                    self.joueur_courant = self.joueurs[1]
                else:
                    print("C'est le tour de : ", self.joueur_courant.nom)
                    ligne, colonne = self.plateau.choisir_prochaine_case(self.joueur_courant.pion)
                    self.plateau.selectionner_case(int(ligne), int(colonne), self.joueur_courant.pion)
                    self.joueur_courant = self.joueurs[1]
            else:
                if (self.joueur_courant.type == "Personne"):
                    ligne, colonne = self.demander_position()
                    self.plateau.selectionner_case(int(ligne), int(colonne), self.joueur_courant.pion)
                    self.joueur_courant = self.joueurs[0]
                else:
                    print("C'est le tour de : ", self.joueur_courant.nom)
                    ligne, colonne = self.plateau.choisir_prochaine_case(self.joueur_courant.pion)
                    self.plateau.selectionner_case(int(ligne), int(colonne), self.joueur_courant.pion)
                    self.joueur_courant = self.joueurs[0]


        elif (choix == 2):  # 2personnes

            if (self.joueur_courant == self.joueurs[0]):
                ligne, colonne = self.demander_position()
                self.plateau.selectionner_case(int(ligne), int(colonne), self.joueur_courant.pion)

            else:
                ligne, colonne = self.demander_position()
                self.plateau.selectionner_case(int(ligne), int(colonne), self.joueur_courant.pion)

    def demander_position(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """

        print(self.joueur_courant.nom, " : Entrez s.v.p. les coordonnées de la case à utiliser: ")
        print("Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? ")
        ligne = self.saisir_nombre(0, 3)
        print("Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? ")
        colonne = self.saisir_nombre(0, 3)

        while (self.plateau.position_valide(int(ligne), int(colonne)) == False):
            print("la position choisie est occupeé ! ")
            print("Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? ")
            ligne = self.saisir_nombre(0, 3)
            print("Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? ")
            colonne = self.saisir_nombre(0, 3)
        return ligne, colonne


if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()
