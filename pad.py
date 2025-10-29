class Pad:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur):  #on définit les caractéristiques de la balle(position, vitesse...)
        """
        Entrée :
            canvas (tk.Canvas) : canevas où dessiner la raquette
            x, y (int|float)    : position du coin supérieur gauche
            largeur, hauteur    : dimensions de la raquette
            couleur (str)       : couleur de remplissage
        Sortie :
            None
        description de la fonction :
            Crée la raquette (rectangle) sur le canevas, initialise ses
            attributs (largeur, hauteur, vitesse) et lie les touches
            gauche/droite aux méthodes de déplacement.
        """
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur)
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse = 40
        self.canvas.bind_all("<Left>", self.deplacer_gauche)                #on associe les déplacements à droite et à gauche aux flèches droite et gauche du clavier
        self.canvas.bind_all("<Right>", self.deplacer_droite)

    def deplacer_gauche(self, event=None):
        """
        Entrée :
            event (tk.Event, optionnel) : événement fourni par Tkinter
        Sortie :
            None
        description de la fonction :
            Déplace la raquette vers la gauche de self.vitesse pixels
            si elle n'atteint pas le bord gauche du canevas.
        """
        if self.canvas.coords(self.id)[0] > 0:                          #tant que la raquette ne dépasse pas du bord gauche du canevas, elle peut se déplacer à gauche
            self.canvas.move(self.id, -self.vitesse, 0)

    def deplacer_droite(self, event=None):
        """
        Entrée :
            event (tk.Event, optionnel) : événement fourni par Tkinter
        Sortie :
            None
        description de la fonction :
            Déplace la raquette vers la droite de self.vitesse pixels
            si elle n'atteint pas le bord droit du canevas.
        """
        if self.canvas.coords(self.id)[2] < self.canvas.winfo_width():  #tant que la raquette ne dépasse pas du bord droit du canevas, elle peut se déplacer à droite
            self.canvas.move(self.id, self.vitesse, 0)

    def coords(self):
        """
        Entrée :
            (aucune)
        Sortie :
            list[float] : [x1, y1, x2, y2] coordonnées de la raquette
        description de la fonction :
            Retourne la position actuelle de la raquette pour la détection de collision.
        """
        return self.canvas.coords(self.id)