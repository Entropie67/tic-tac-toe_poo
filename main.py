

class Case:
    """
    classe case, une case possède trois états None, 0 ou 1. 
    None signifie que la case est vide, 0 signifie que la case est occupée par un pion du joueur 0 et 1 signifie que la case est occupée par un pion du joueur 1. 
    
    """
    def __init__(self):
        self.etat = None
    
    def getEtat(self):
        return self.etat

    def setEtat(self, etat):
        self.etat = etat




class Grille:
    """Une grille est une matrice 9x9 de cases. Elle est initialisée avec des cases vides."""
    pass