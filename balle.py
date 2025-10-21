import random as rd
from math import sqrt

class Balle:
    def __init__(self, canvas, x, y, rayon, couleur, vx=5, vy=-5):
        self.canvas = canvas
        self.id = canvas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill=couleur)
        self.vx = vx
        self.vy = vy
        self.rayon = rayon

    def deplacer(self):
        self.canvas.move(self.id, self.vx, self.vy)
        self.verifier_collisions_bords()

    def coords(self):
        return self.canvas.coords(self.id)

    def inverser_vx(self):
        self.vx = -self.vx 

    def inverser_vy(self):
        self.vy = -self.vy

    def verifier_collisions_bords(self):
        x1, y1, x2, y2 = self.coords()
        if x1 <= 0 or x2 >= self.canvas.winfo_width():
            self.inverser_vx()
        if y1 <= 0:
            self.inverser_vy()

    def augmenter_vitesse(self):

        facteur = 1.05
        vitesse_max = 20.0
        vitesse = sqrt(self.vx ** 2 + self.vy ** 2)
        if vitesse == 0:
            return 0.0
        nouvelle_vitesse = min(vitesse * facteur, vitesse_max)
        échelle = nouvelle_vitesse / vitesse
        self.vx *= échelle
        self.vy *= échelle
        return nouvelle_vitesse