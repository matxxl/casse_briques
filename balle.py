import random as rd
from math import sqrt

class Balle:
    def __init__(self, canvas, x, y, rayon, couleur, vx = 5 * rd.random(), vy = -5 * rd.random()):  #on définit les caractéristiques de la balle(position, vitesse...)
        """
        Entrée :
            canvas (tk.Canvas) : canevas où dessiner la balle
            x, y (int|float)    : position du centre de la balle
            rayon (int|float)   : rayon de la balle
            couleur (str)       : couleur de la balle
            vx, vy (float, optionnel) : composantes de vitesse initiales
        Sortie :
            None
        description de la fonction :
            Crée l'oval représentant la balle sur le canevas et initialise
            les composantes de vitesse et le rayon.
        """
        self.canvas = canvas                                                                #on écrit ces égalités pour que la classe puisse être exploitée par le code principal
        self.id = canvas.create_oval(x-rayon, y-rayon, x+rayon, y+rayon, fill=couleur)
        self.vx = vx
        self.vy = vy
        self.rayon = rayon

    def deplacer(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Déplace la balle selon ses composantes de vitesse (vx, vy)
            puis vérifie la collision avec les bords du canevas.
        """
        self.canvas.move(self.id, self.vx, self.vy)
        self.verifier_collisions_bords()            #vérifier s'il y a collision à chaque déplacement

    def coords(self):                               #on récupère les coordonnées de la balle
        """
        Entrée :
            (aucune)
        Sortie :
            list[float] : [x1, y1, x2, y2] coordonnées de l'oval (balle)
        description de la fonction :
            Retourne les coordonnées actuelles de la balle sur le canevas.
        """
        return self.canvas.coords(self.id)

    def inverser_vx(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Inverse la composante horizontale de la vitesse (rebond horizontal).
        """
        self.vx = -self.vx 

    def inverser_vy(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Inverse la composante verticale de la vitesse (rebond vertical).
        """
        self.vy = -self.vy

    def verifier_collisions_bords(self):
        """
        Entrée :
            (aucune)
        Sortie :
            None
        description de la fonction :
            Vérifie les collisions de la balle avec les bords du canevas.
            Inverse vx si la balle touche le bord gauche/droit, inverse vy
            si elle touche le bord supérieur. La sortie par le bas n'est pas
            gérée ici (traitée dans la logique de jeu principale).
        """
        x1, y1, x2, y2 = self.coords()
        if x1 <= 0 or x2 >= self.canvas.winfo_width():              #la direction de la balle change à chaque fois qu'elle tape un bord du canevas
            self.inverser_vx()
        if y1 <= 0:
            self.inverser_vy()

    def augmenter_vitesse(self):                           #on veut faire de sorte à ce que la balle augmente un peu en vitesse à chaque collision avec la raquette
        """
        Entrée :
            (aucune)
        Sortie :
            float : nouvelle vitesse scalaire (ou 0.0 si vitesse initiale = 0)
        description de la fonction :
            Augmente la vitesse globale de la balle d'un facteur fixe
            tout en limitant la vitesse à vitesse_max. Met à l'échelle
            les composantes vx/vy pour conserver la direction.
        """
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