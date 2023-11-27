

class Case:
    """
    classe case, une case possède trois états None, 0 ou 1. 
    None signifie que la case est vide, 0 signifie que la case est occupée par un pion du joueur 0 et 1 signifie que la case est occupée par un pion du joueur 1. 
    
    """
    def __init__(self, etat=None):
        self.etat = etat
    
    def getEtat(self):
        return self.etat

    def setEtat(self, etat):
        self.etat = etat

    def __str__(self):
        return str(self.etat if self.etat is not None else ' ')




class Grille:
    """Une grille est une matrice 9x9 de cases. Elle est initialisée avec des cases vides."""
    def __init__(self):
        self.grille = [[Case() for i in range(3)] for j in range(3)]    # matrice 3x3 de cases


    def affichage(self):
        """Affiche la grille dans la console."""
        print('  0 1 2 3 4 5 6 7 8')
        for i in range(9):
            print(i, end=' ')
            for j in range(9):
                print(self.grille[i][j], end=' ')
            print()

    def _check(self, i, j):
        """Vérifie si la case (i, j) est vide."""
        return self.grille[i][j].getEtat() is None  

    def set(self, i, j, etat):
        """Change l'état de la case (i, j) par etat (0 ou 1).seulement si l'état est None"""
        if self._check(i, j):
            self.grille[i][j].setEtat(etat)
        

    def pleine(self):
        """Vérifie si la grille est pleine."""
        for i in range(9):
            for j in range(9):
                if self.check(i, j):
                    return False
        return True



class Jeu:

    """ Cette classe permet de jouer au jeu de Hex. Elle possède une grille et deux joueurs. """    

    def ___init__(self):
        self.grille = Grille()
        self.joueur0 = Joueur(0)
        self.joueur1 = Joueur(1)
        self.joueurCourant = self.joueur0



    def jouer(self):
        """Fait jouer les joueurs à tour de rôle."""
        while not self.grille.pleine():
            self.grille.affichage()
            print('Au tour du joueur', self.joueurCourant.getNumero())
            i, j = self.joueurCourant.jouer()
            self.grille.set(i, j, self.joueurCourant.getNumero())
            if self.gagne():
                print('Le joueur', self.joueurCourant.getNumero(), 'a gagné !')
                break
            self.joueurCourant = self.joueur0 if self.joueurCourant == self.joueur1 else self.joueur1   # changement de joueur  
       