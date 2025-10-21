import tkinter as tk
import random as rd
import raquette as rq
import brique_mat as br
import ball_mat as ba

class Casse_briques:
    def __init__(self):
        root = tk.Tk()
        root.title("Casse Briques")
        self.canvas = tk.Canvas(root, width = 900, height = 500, bg ='black')
        self.canvas.grid(row = 1, column = 0, columnspan = 3)
        self.label_vies = tk.Label(root, text = "Vies : 3")
        self.label_vies.grid(row = 0, column = 1, columnspan = 3)
        self.label_score = tk.Label(root, text = "Score : 0")
        self.label_score.grid(row = 0, column = 0, columnspan = 3)
        self.bouton = tk.Button(root, text = "Quitter", command = root.destroy)
        self.bouton.grid(row = 2, column = 1)

        self.vies = 3
        self.score = 0
        self.briques = []
        self.creer_briques()
        self.balle = ba.Balle(self.canvas, 450, 400, 10, "#FFFFFF")
        self.raquette = rq.Raquette(self.canvas)
        root.bind("<Left>", self.raquette.left1)
        root.bind("<Right>", self.raquette.right1)
        root.mainloop()

    def creer_briques(self):
        couleurs = ["red", "orange", "yellow", "green"]
        for i in range(5):
            for j in range(10):
                brique = br.Brique(self.canvas, 10+j*85, 30+i*25, 80, 20, rd.choice(couleurs))
                self.briques.append(brique)
    
    def verifier_collision(self, obj):
        x1, y1, x2, y2 = self.balle.coords()
        x3, y3, x4, y4 = obj.coords()
        return not (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4)
    
    def jouer(self):
        self.balle.deplacer()
        # Collision avec le pad
        if self.verifier_collision(self.pad):
            self.balle.inverser_vy()

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
            self.vies -= 1
            self.label_vies.config(text=f"Vies : {self.vies}")
            if self.vies > 0:
                # Remettre la balle au centre
                self.canvas.coords(self.balle.id, 440, 390, 460, 410)
                self.balle.vx = 5
                self.balle.vy = -5
            else:
                self.canvas.create_text(450, 250, text="Tu as perdu !", fill="white", font=("Helvetica", 30))
                return

        # Relancer la boucle
        self.root.after(20, self.jouer)

if __name__ == "__main__" :
    app = Casse_briques()
