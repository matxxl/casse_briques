class Brique:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur):
        """
        Entrée :
            canvas (tk.Canvas) : canevas où dessiner la brique
            x, y (int|float)    : position du coin supérieur gauche
            largeur, hauteur    : dimensions du rectangle
            couleur (str)       : couleur de remplissage
        Sortie :
            None
        description de la fonction :
            Crée un rectangle sur le canevas pour représenter une brique
            et stocke son identifiant dans self.id.
        """
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur)

    def detruire(self):                 #fonction supprimant le canvas de la brique en cas de collision avec la balle
        """
        Entrée :
            (aucune) -- utilise self.canvas et self.id
        Sortie :
            None
        description de la fonction :
            Supprime l'objet graphique correspondant à la brique du canevas.
        """
        self.canvas.delete(self.id)

    def coords(self):
        """
        Entrée :
            (aucune) -- utilise self.canvas et self.id
        Sortie :
            list[float] : [x1, y1, x2, y2] coordonnées du rectangle
        description de la fonction :
            Retourne les coordonnées actuelles de la brique sur le canevas.
        """
        return self.canvas.coords(self.id)  # retourne les coordonnées des coins de la brique