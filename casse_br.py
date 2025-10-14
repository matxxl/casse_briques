import tkinter as tk
import random

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


class Pad:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur)
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse = 20
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


class Brique:
    def __init__(self, canvas, x, y, largeur, hauteur, couleur):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x+largeur, y+hauteur, fill=couleur)
        self.vie = 1

    def detruire(self):
        self.canvas.delete(self.id)

    def coords(self):
        return self.canvas.coords(self.id)  # <-- Ajouté pour retourner les coordonnées


class Casse_briques:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Casse Briques")
        self.canvas = tk.Canvas(self.root, width=900, height=500, bg='black')
        self.canvas.grid(row=1, column=0, columnspan=3)
        self.label_vies = tk.Label(self.root, text="Vies : 3", fg='white', bg='black')
        self.label_vies.grid(row=0, column=1)
        self.label_score = tk.Label(self.root, text="Score : 0", fg='white', bg='black')
        self.label_score.grid(row=0, column=0)
        self.bouton = tk.Button(self.root, text="Quitter", command=self.root.destroy)
        self.bouton.grid(row=2, column=1)

        # Initialisation jeu
        self.vies = 3
        self.score = 0
        self.balle = Balle(self.canvas, 450, 400, 10, "white")
        self.pad = Pad(self.canvas, 400, 450, 100, 10, "blue")
        self.briques = []
        self.creer_briques()

        # Boucle principale
        self.jouer()
        self.root.mainloop()

    def creer_briques(self):
        couleurs = ["red", "orange", "yellow", "green"]
        for i in range(5):
            for j in range(10):
                brique = Brique(self.canvas, 10+j*85, 30+i*25, 80, 20, random.choice(couleurs))
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
                self.canvas.create_text(450, 250, text="GAME OVER", fill="white", font=("Arial", 30))
                return

        # Relancer la boucle
        self.root.after(20, self.jouer)


if __name__ == "__main__":
    app = Casse_briques()
