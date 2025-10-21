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
        self.bouton_rejouer = tk.Button(self.root, text = "Rejouer", command = self.rejouer, fg = 'white', bg = "#FF00E6")
        self.bouton_rejouer.grid(row = 6, column = 0)
        self.bouton_quitter = tk.Button(self.root, text = "Quitter", command = self.root.destroy, fg = 'white', bg = "#FF00E6")
        self.bouton_quitter.grid(row = 6, column = 1)
        self.bouton_jouer = tk.Button(self.root, text = "Jouer", command = self.jouer, fg = 'white', bg = "#FF00E6")
        self.bouton_jouer.grid(row = 6, column = 2)

        # Initialisation jeu
        self.vies = 3
        self.score = 0
        self.balle = Balle(self.canvas, 450, 400, 10, "#FFFFFF")
        self.pad = Pad(self.canvas, 400, 450, 150, 7, "#00FFC8")
        self.briques = []
        self.creer_briques()

        # Boucle principale lancée si le bouton jouer est cliqué
        if self.bouton_jouer == True :
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

        # on considère le centre et le rayon
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2

        # coordonnées de l'objet
        x3, y3, x4, y4 = obj.coords()

        # collision si le cercle touche le rectangle
        return not (cx + rayon < x3 or cx - rayon > x4 or cy + rayon < y3 or cy - rayon > y4)


    def jouer(self):
        
        self.balle.deplacer()
                
        # Collision avec le pad     
        if self.verifier_collision(self.pad):
            self.balle.inverser_vy()
            self.balle.augmenter_vitesse()

        # Collision avec les briques
        for brique in self.briques[:]:
            if self.verifier_collision(brique):
                brique.detruire()
                self.briques.remove(brique)
                self.balle.inverser_vy()
                self.score += 10
                self.label_score.config(text=f"Score : {self.score}")

        # Balle tombée
        if self.balle.coords()[3] >= self.canvas.winfo_height():
            # Mettre à jour le compteur
            if self.vies >= 0 :
                self.vies -= 1
                self.label_vies.config(text = f"Vies : {self.vies}")
            # Ne pas avoir un score négatif
            elif self.vies <= -1 :
                self.label_vies.config(text = "Vies : 0")
            
            
            
            if self.vies >= 0 :
                # Remettre la balle au centre
                self.canvas.coords(self.balle.id, 440, 390, 460, 410)
                self.balle.vx = 2.5 * (1 + random.random())  # Vitesse horizontale aléatoire
                self.balle.vy = -2.5 * (1 + random.random()) # Vitesse verticale aléatoire
            elif self.score == 500:
                self.message_1 = self.canvas.create_text(450, 250, text = "Tu as gagné !", fill = "white", font = ("Helvetica", 30))
                return
            else:
                self.label_vies.config(text = "Vies : 0")
                self.message_2 = self.canvas.create_text(450, 250, text = "Tu as perdu !", fill = "white", font = ("Helvetica", 30))
                return

        # Relancer la boucle
        self.root.after(10, self.jouer)

    def rejouer(self):
        # Réinitialiser les variables du jeu
        self.vies = 3
        self.score = 0
        self.label_vies.config(text = f"Vies : {self.vies}")
        self.label_score.config(text=f"Score : {self.score}")

        # Réinitialiser la balle
        self.canvas.coords(self.balle.id, 440, 390, 460, 410)
        self.balle.vx = 2.5 * (1 + random.random())
        self.balle.vy = -2.5 * (1 + random.random())

        # Réinitialiser les briques
        for brique in self.briques:
            brique.detruire()
        self.briques.clear()
        self.creer_briques()

        # Effacer le message de victoire ou défaite
        if hasattr(self, 'message_1'):
            self.canvas.delete(self.message_1)
            del self.message_1
        if hasattr(self, 'message_2'):
            self.canvas.delete(self.message_2)
            del self.message_2

if __name__ == "__main__" :
    app = Casse_briques()


