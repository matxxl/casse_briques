class Brique:
    def __init__(self, canvas, x, y, longueur, largeur, couleur):
        self.canvas = canvas
        self.brique = canvas.create_rectangle(x, y, x + longueur, y + largeur, fill=couleur)

    def detruire_brique(self):
        self.canvas.delete(self.brique)

    def coords(self):
        return self.canvas.coords(self.brique)