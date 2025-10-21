import tkinter as tk
import random
from random import randint
from balle import *
from pad import *
from brique import *

class Casse_briques:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Casse Briques")
        self.canvas = tk.Canvas(self.root, width = 900, height = 500, bg = 'black')
        self.canvas.grid(row = 1, column = 0, columnspan = 3)
        self.label_vies = tk.Label(self.root, text = "Vies : 3", fg = 'black', bg = 'white')
        self.label_vies.grid(row = 0, column = 1)
        self.label_score = tk.Label(self.root, text = "Score : 0", fg = 'black', bg = 'white')
        self.label_score.grid(row = 0, column = 0)
        self.bouton_quitter = tk.Button(self.root, text = "Quitter", command = self.root.destroy)
        self.bouton_quitter.grid(row = 2, column = 1)

        # Initialisation jeu
        self.vies = 3
        self.score = 0
        self.balle = Balle(self.canvas, 450, 400, 10, "#FFFFFF")
        self.pad = Pad(self.canvas, 400, 450, 100, 10, "blue")
        self.briques = []
        self.creer_briques()

        # Boucle principale
        self.jouer()
        self.root.mainloop()

    def creer_briques(self):
        couleurs = ["red", "orange", "yellow", "green", "blue"]
        for i in range(5):
            for j in range(10):
                brique = Brique(self.canvas, 10 + j * 85, 30 + i * 25, 83, 23, random.choice(couleurs))
                self.briques.append(brique)

    def verifier_collision(self, obj):
        # coordonnées de la balle
        x1, y1, x2, y2 = self.balle.coords()
        rayon = self.balle.rayon

        # centre de la balle
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2

        # coordonnées de l'objet (rectangle)
        x3, y3, x4, y4 = obj.coords()

        # centre et demi-dimensions du rectangle
        rx = (x3 + x4) / 2
        ry = (y3 + y4) / 2
        half_w = (x4 - x3) / 2
        half_h = (y4 - y3) / 2

        # distances absolues entre centres
        dx = abs(cx - rx)
        dy = abs(cy - ry)

        # chevauchement sur chaque axe, si positif il y a collision
        chevauch_x = rayon + half_w - dx
        chevauch_y = rayon + half_h - dy

        if chevauch_x > 0 and chevauch_y > 0:
            # collision détectée ; déterminer l'axe principal de pénétration
            # si la pénétration en x est plus petite, la collision est latérale (inverser vx)
            if chevauch_x < chevauch_y:
                return True, 'x'
            else:
                return True, 'y'
        return False, None


    def jouer(self):
        self.balle.deplacer()
        # Collision avec le pad
        collision, axis = self.verifier_collision(self.pad)
        if collision:
            if axis == 'x':
                self.balle.inverser_vx()
            else:
                self.balle.inverser_vy()
                self.balle.augmenter_vitesse()

        # Collision avec les briques
        for brique in self.briques[:]:
            collision, axis = self.verifier_collision(brique)
            if collision:
                brique.detruire()
                self.briques.remove(brique)
                if axis == 'x':
                    self.balle.inverser_vx()
                else:
                    self.balle.inverser_vy()
                self.score += 10
                self.label_score.config(text=f"Score : {self.score}")

        # Balle tombée
        if self.balle.coords()[3] >= self.canvas.winfo_height():
            self.vies -= 1
            self.label_vies.config(text=f"Vies : {self.vies}")
            if self.vies > -1:
                # Remettre la balle au centre
                self.canvas.coords(self.balle.id, 440, 390, 460, 410)
                self.balle.vx = 5*(1+random.random())  # Vitesse horizontale aléatoire
                self.balle.vy = -5*(1+random.random()) # Vitesse verticale aléatoire
            elif self.score == 500:
                self.canvas.create_text(450, 250, text = "Tu as gagné !", fill = "white", font = ("Helvetica", 30))
                return
            else:
                self.canvas.create_text(450, 250, text = "Tu as perdu !", fill = "white", font = ("Helvetica", 30))
                return

        # Relancer la boucle
        self.root.after(20, self.jouer)


if __name__ == "__main__":
    app = Casse_briques()
