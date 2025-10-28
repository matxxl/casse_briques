import tkinter as tk
import random
from random import randint
from balle import *
from pad import *
from brique import *

class Casse_briques:
    def __init__(self):                    #on initialise la fenêtre, l'affichage et les boutons
        self.root = tk.Tk()                # on crée la racine de la fenêtre
        self.root.title("Casse Briques")
        self.canvas = tk.Canvas(self.root, width = 900, height = 500, bg = 'black')     #on crée la fenêtre
        self.canvas.grid(row = 1, column = 0, columnspan = 3)   #on organise la fenêtre sous forme de grille (plus simple pour placer les éléments)
        self.label_vies = tk.Label(self.root, text = "Vies : 3", fg = 'black', bg = 'white')
        self.label_vies.grid(row = 0, column = 2)
        self.label_score = tk.Label(self.root, text = "Score : 0", fg = 'black', bg = 'white')
        self.label_score.grid(row = 0, column = 0)
        self.label_meilleur_score = tk.Label(self.root, text = "Meilleur score : 0", fg = 'black', bg = 'white')
        self.label_meilleur_score.grid(row = 0, column = 1)
        self.scores_precedents = []  # pile pour stocker les scores et afficher le meilleur
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
        self.pad = Pad(self.canvas, 400, 450, 100, 7, "#00FFC8")
        self.briques = []
        self.creer_briques()

        # Boucle principale lancée si le bouton jouer est cliqué
        if self.bouton_jouer == True :
                self.jouer()
        self.root.mainloop()

    def creer_briques(self):
        couleurs = ["red", "blue", "yellow", "green", "white"]
        for i in range(5):
            for j in range(10):
                brique = Brique(self.canvas, 10 + j * 85, 30 + i * 25, 80, 20, couleurs[i])
                self.briques.append(brique)

    def verifier_collision(self, obj):
        
        x1, y1, x2, y2 = self.balle.coords()        #on récupère les coordonnées de la balle
        rayon = self.balle.rayon

        cx = (x1 + x2) / 2                          # centre de la balle
        cy = (y1 + y2) / 2

        x3, y3, x4, y4 = obj.coords()               # coordonnées de l'objet (rectangle)

  
        rx = (x3 + x4) / 2                          # centre du rectangle
        ry = (y3 + y4) / 2
        half_w = (x4 - x3) / 2                      # demi-dimensions  du rectangle
        half_h = (y4 - y3) / 2

        dx = abs(cx - rx)                           # distances absolues entre le centre de la balle et du rectangle
        dy = abs(cy - ry)

        chevauch_x = rayon + half_w - dx            # chevauchement sur chaque axe, si positif il y a collision
        chevauch_y = rayon + half_h - dy

        if chevauch_x > 0 and chevauch_y > 0:
            # Si il y a collision, on essaie de déterminer l'axe principal de pénétration
            # si la pénétration en x est plus petite, la collision est latérale (inverser vx) (marche pour les rectangles de petite largeur)
            if chevauch_x < chevauch_y:
                return True, 'x'
            else:
                return True, 'y'
        return False, None


    def jouer(self):
        
        self.balle.deplacer()
        collision, axis = self.verifier_collision(self.pad) # on vérifie s'il y a collision avec le pad
        if collision:
            if axis == 'x':                     # on inverse la composante selon l'axe détecté
                self.balle.inverser_vx()    
            else:
                self.balle.inverser_vy()
            self.balle.augmenter_vitesse()      #on augmente légèrement la vitesse après contact

        # Collision avec les briques
        for brique in self.briques[:]:
            collision, axis = self.verifier_collision(brique)
            if collision:
                brique.detruire()               #le canvas de la brique se supprime après collision
                self.briques.remove(brique)     #on enlève la brique détruite de la liste contenant les canvas des briques
                if axis == 'x':
                    self.balle.inverser_vx()
                else:
                    self.balle.inverser_vy()
                self.score += 10
                self.label_score.config(text=f"Score : {self.score}")

        # Cas où la balle tombe
        if self.balle.coords()[3] >= self.canvas.winfo_height(): #coordonnée y2 (le bas de la balle) sort du canevas
            if self.vies >= 0 :                     # Mettre à jour le compteur
                self.vies -= 1
                self.label_vies.config(text = f"Vies : {self.vies}")
            elif self.vies <= -1 :                  # Ne pas avoir un score négatif
                self.label_vies.config(text = "Vies : 0")
            
            
            
            if self.vies >= 0 :
                # la balle se remet au centre
                self.canvas.coords(self.balle.id, 440, 390, 460, 410)
                self.balle.vx = 2.5 * (1 + random.random())  # Vitesse horizontale aléatoire
                self.balle.vy = -2.5 * (1 + random.random()) # Vitesse verticale aléatoire
            elif self.score == 500:  #message de victoire en cas de score égal à 500
                self.message_1 = self.canvas.create_text(450, 250, text = "Tu as gagné !", fill = "white", font = ("Helvetica", 30))
                self.sauvegarder_score()
                return
            else:
                self.label_vies.config(text = "Vies : 0")
                self.message_2 = self.canvas.create_text(450, 250, text = "Tu as perdu !", fill = "white", font = ("Helvetica", 30))
                self.sauvegarder_score()
                return

    
        self.root.after(10, self.jouer) #on relance la boucle

    def sauvegarder_score(self):
        self.scores_precedents.append(self.score) # on ajoute le score actuel à la pile
        if len(self.scores_precedents) > 15: # on garde seulement les 15 derniers scores pour la mémoire
            self.scores_precedents.pop(0)
        meilleur_score = max(self.scores_precedents)# le meilleur score est mis à jour
        self.label_meilleur_score.config(text=f"Meilleur score : {meilleur_score}")

    def rejouer(self):

        # Réinitialisation des variables du jeu
        self.vies = 3
        self.score = 0
        self.label_vies.config(text = f"Vies : {self.vies}")
        self.label_score.config(text=f"Score : {self.score}")

        # Réinitialisation des coordonnées de la balle
        self.canvas.coords(self.balle.id, 440, 390, 460, 410)
        self.balle.vx = 2.5 * (1 + random.random())
        self.balle.vy = -2.5 * (1 + random.random())

        # Réinitialisation des briques
        for brique in self.briques:
            brique.detruire()
        self.briques.clear()
        self.creer_briques()

        # Suppression du message de victoire ou défaite
        if hasattr(self, 'message_1'):
            self.canvas.delete(self.message_1)
            del self.message_1
        if hasattr(self, 'message_2'):
            self.canvas.delete(self.message_2)
            del self.message_2

if __name__ == "__main__" :
    app = Casse_briques()


