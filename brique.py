class Brique:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur)
        self.vie = 1

    def detruire(self):
        self.canvas.delete(self.id)

    def coords(self):
        return self.canvas.coords(self.id)  # Ajouté pour retourner les coordonnées