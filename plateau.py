__authors__ = "Amani Miled Azer Taboubi"
__date__ = "le 5 janvier 2019"

"""
Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire !
"""

from case import Case
import random

class Plateau:
    """
    Classe modélisant le plateau du jeu Tic-Tac-Toe.

    Attributes:
        cases (dictionary): Dictionnaire de cases. La clé est une position (ligne, colonne),
                            et la valeur est une instance de la classe Case.
    """
    cases = {}

    def __init__(self):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        """
        Méthode fournie permettant d'initialiser le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")

    def __str__(self):
        """Méthode spéciale fournie indiquant à Python comment représenter une instance de Plateau
        sous la forme d'une chaîne de caractères. Permet donc d'afficher le plateau du jeu
        à l'écran en faisant par exemple:
        p1 = Plateau()
        print(p1)
        Donc, lorsque vous affichez un objet, Python invoque automatiquement la méthode __str__
        Voici un exemple d'affichage:
         +-0-+-1-+-2-+
        0|   | X | X |
         +---+---+---+
        1| O | O | X |
         +---+---+---+
        2|   |   | O |
         +---+---+---+

        Returns:
            string: Retourne la chaîne de caractères à afficher.
        """
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i)+ "| "
            for j in range(0, 3):
                s += self.cases[(i,j)].contenu + " | "
            if i<=1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s
        

    def non_plein(self):
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
        test = False
        i = 0
        j = 0

        while i < 3 and test == False:
            while j < 3 and test == False:
                if (self.cases[i, j].contenu == ' '):
                    test = True
                j += 1
            i += 1

        return test
        

    def position_valide(self, ligne, colonne):
        """
        Vérifie si une position est valide pour jouer.
        La position ne doit pas être occupée.
        Il faut utiliser la méthode est_vide() de la classe Case.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.

        Returns:
            bool: True si la position est valide, False autrement.
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."

        test = self.cases[(int(ligne),int(colonne))].est_vide()

        return test
        
        

    def selectionner_case(self, ligne, colonne, pion):
        """
        Permet de modifier le contenu de la case
        qui a les coordonnées (ligne,colonne) dans le plateau du jeu
        en utilisant la valeur de la variable pion.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.
            pion (string): Une chaîne de caractères ("X" ou "O").
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        self.cases[(ligne,colonne)].contenu = pion
       


    def est_gagnant(self, pion):
        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        i = 0
        for i in range(3):
            if self.cases[(0, i)].contenu == self.cases[(1, i)].contenu == self.cases[(2, i)].contenu == pion:
                return True
            elif self.cases[(i, 0)].contenu == self.cases[(i, 1)].contenu == self.cases[(i, 2)].contenu == pion:
                return True

        if self.cases[(0, 0)].contenu == self.cases[(1, 1)].contenu == self.cases[(2, 2)].contenu == pion:
            return True
        elif self.cases[(0, 2)].contenu == self.cases[(1, 1)].contenu == self.cases[(2, 0)].contenu == pion:
            return True
        else:
            return False
    
    def cas_general(self,pion):
        # Méthode implémentée pour simplifier le choix prochain de l'ordinateur pendant la partie
        # Utilisée dans la méthode choisir_prochaine_case(pion)

        ligne = 0
        colonne = 0
        
        c=0
        vide=0
        vide_l=0
        vide_c=0

        case1 =False
        case2 = False
        case3 = False
        """------ First Case ------"""
        
        for i in range (0,3):
            for j in range (0,3):
                if( self.cases[(i,j)].est_pion(pion) ):
                    c += 1
                if ( self.cases[(i,j)].est_vide() ):
                    vide +=1
                    vide_l = i
                    vide_c = j
            if( (c ==2) and (vide == 1) ):

                case1 =True
                case2 = True
                case3 = True
                ligne = vide_l
                colonne = vide_c
                break
            else:
                c = 0
                vide = 0
                vide_l = 0
                vide_c = 0
        
        if( case1 == False ):
            """------ 2eme cas ------"""
            
            for i in range (0,3):
                for j in range (0,3):
                    if( self.cases[(j,i)].est_pion(pion) ):
                        c += 1
                    if ( self.cases[(j,i)].est_vide() ):
                        vide +=1
                        vide_l = j
                        vide_c = i
                        
                if( (c ==2) and (vide == 1) ):
                    case1 =True
                    case2 = True
                    case3 = True
                    
                    ligne = vide_l
                    colonne = vide_c
                    break
                else:
                    c = 0
                    vide = 0
                    vide_l = 0
                    vide_c = 0
        if (case2 == False ):
            """------ 3eme cas ------"""
           
            i = 0
            j = 0
            while ( (i<=2) and (j<=2)):
                if( self.cases[(i,j)].est_pion(pion) ):
                    c += 1
                    
                if ( self.cases[(i,j)].est_vide() ):
                    vide +=1
                    vide_l = i
                    vide_c = j

                i += 1
                j += 1
                     
            if( (c ==2) and (vide == 1) ):
                case1 = True
                case2 = True
                case3 = True
                    
                ligne = vide_l
                colonne = vide_c
            else:
                c = 0
                vide = 0
                vide_l = 0
                vide_c = 0
                
        if (case3 == False ):
            
            """------ 4eme cas ------"""
            
            i = 0
            j = 2
            while ( (i<=2) and (j>=0)):
                if( self.cases[(i,j)].est_pion(pion) ):
                    c += 1
                    
                if ( self.cases[(i,j)].est_vide() ):
                    vide +=1
                    vide_l = i
                    vide_c = j
                    
                    
                i += 1
                j -= 1
                     
            if( (c ==2) and (vide == 1) ):
                ligne = vide_l
                colonne = vide_c
                case1 = True
                case2 = True
                case3 = True
            else:
                
                c = 0
                vide = 0
                vide_l = 0
                vide_c = 0
                case1 = False
                case2 = False
                case3 = False
                
        if ( (case1 == False) and (case2 == False) and (case3 == False)):
                ligne = -1
                colonne = -1


        return (ligne,colonne)

        
        
    def choisir_prochaine_case(self, pion):
        """
        Permet de retourner les coordonnées (ligne, colonne) de la case que l'ordinateur
        peut choisir afin de jouer contre un autre joueur qui est normalement une personne.
        Ce choix doit se faire en fonction de la configuration actuelle du plateau.
        L'algorithme que vous allez concevoir permettant de faire jouer l'ordinateur
        n'a pas besoin d'être optimal. Cela permettra à l'adversaire de gagner de temps en temps.
        Il faut par contre essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'adversaire pour que ce dernier ne gagne pas facilement.
        Il faut aussi essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'ordinateur pour que ce dernier puisse gagner.
        Vous pouvez utiliser ici la fonction randrange() du module random.
        Par exemple: randrange(1,10) vous retourne une valeur entre 1 et 9 au hasard.

        Args:
            pion (string): La forme du pion de l'adversaire de l'ordinateur ("X" ou "O").

        Returns:
            (int,int): Une paire d'entiers représentant les coordonnées de la case choisie.
        """
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        ligne = -1
        colonne = -1
        l,c = self.cas_general(pion)

        if((l >= 0 ) and (c >=0)):
            ligne = l
            colonne = c
        else:
            if(pion == "O"):
                l,c = self.cas_general("X")
                if((l >= 0 ) and (c >=0)):
                    ligne = l
                    colonne = c
                    print(ligne)
                    print(colonne)
                    
            if(pion == "X"):
                l,c = self.cas_general("O")
                if((l >= 0 ) and (c >=0)):
                    ligne = l
                    colonne = c
                    print(ligne)
                    print(colonne)

        if((ligne < 0) and (colonne < 0)):
            l = random.randint(0,2)
            c = random.randint(0,2)
            while (self.cases[(l,c)].est_vide() == False):
                l = random.randint(0,2)
                c = random.randint(0,2)

            ligne = l
            colonne = c

            
        return ligne,colonne
            

            
            
        

        
                    
            

        
