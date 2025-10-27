class Brique:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur)

    def detruire(self):                 #fonction supprimant le canvas de la brique en cas de collision avec la balle
        self.canvas.delete(self.id)

    def coords(self):
        return self.canvas.coords(self.id)  # retourne les coordonnées des coins de la brique