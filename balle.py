import random as rd
from math import sqrt

class Balle:
    def __init__(self, canvas, x, y, rayon, couleur, vx = 5 * rd.random(), vy = -5 * rd.random()):  #on définit les caractéristiques de la balle(position, vitesse...)
        self.canvas = canvas                                                                #on écrit ces égalités pour que la classe puisse être exploitée par le code principal
        self.id = canvas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill=couleur)
        self.vx = vx
        self.vy = vy
        self.rayon = rayon

    def deplacer(self):
        self.canvas.move(self.id, self.vx, self.vy)
        self.verifier_collisions_bords()            #vérifier s'il y a collision à chaque déplacement

    def coords(self):                               #on récupère les coordonnées de la balle
        return self.canvas.coords(self.id)

    def inverser_vx(self):
        self.vx = -self.vx 

    def inverser_vy(self):
        self.vy = -self.vy

    def verifier_collisions_bords(self):
        x1, y1, x2, y2 = self.coords()
        if x1 <= 0 or x2 >= self.canvas.winfo_width():              #la direction de la balle change à chaque fois qu'elle tape un bord du canevas
            self.inverser_vx()
        if y1 <= 0:
            self.inverser_vy()

    def augmenter_vitesse(self):                           #on veut faire de sorte à ce que la balle augmente un peu en vitesse à chaque collision avec la raquette

        facteur = 1.05
        vitesse_max = 20.0
        vitesse = sqrt(self.vx ** 2 + self.vy ** 2)         #on prend une même vitesse globale selon x et y
        if vitesse == 0:                                    #on prend le cas vitesse=0 à part sinon échelle ne peut pas être calculé (division par 0)
            return 0.0
        nouvelle_vitesse = min(vitesse * facteur, vitesse_max)
        échelle = nouvelle_vitesse / vitesse
        self.vx *= échelle
        self.vy *= échelle
        return nouvelle_vitesse