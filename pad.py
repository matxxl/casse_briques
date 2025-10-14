class Pad:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur)
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse = 40
        self.canvas.bind_all("<Left>", self.deplacer_gauche)
        self.canvas.bind_all("<Right>", self.deplacer_droite)

    def deplacer_gauche(self, event=None):
        if self.canvas.coords(self.id)[0] > 0:
            self.canvas.move(self.id, -self.vitesse, 0)

    def deplacer_droite(self, event=None):
        if self.canvas.coords(self.id)[2] < self.canvas.winfo_width():
            self.canvas.move(self.id, self.vitesse, 0)

    def coords(self):
        return self.canvas.coords(self.id)