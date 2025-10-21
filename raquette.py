from tkinter import *

class Raquette:
    def __init__(self, canvas):
        self.x = 450
        self.y = 450
        self.canvas = canvas
        self.raquette = canvas.create_rectangle(self.x, self.y, self.x + 100, self.y +15, fill = 'orange')
    
    '''def left(self, event):
        x = -10
        y=0
        self.canvas.move(self.raquette, x, y)
    
    def right(self, event):
        x = 10
        y = 0
        self.canvas.move(self.raquette, x, y)'''

    def left1(self, event):
        x1,y1,x2,y2 = self.canvas.coords(self.raquette)            #on prend les coordonnées de la raquette
        if x1 > 0:                                                 #tant que le bord gauche de la raquette ne dépasse pas la bordure gauche de la fenêtre, on peut la déplacer à gauche
            x = -10
            if x1 + x <0:                                          #boucle permettant de ramener à x1 = 0 si x1 dépasse à gauche
                x = -x1
            self.canvas.move(self.raquette, x, 0)

    def right1(self, event):
        x1,y1,x2,y2 = self.canvas.coords(self.raquette)             #on prend les coordonnées de la raquette
        if x2 < 900:                                                #tant que le bord droit de la raquette ne dépasse pas la bordure droite de la fenêtre (x=200), on peut la déplacer à droite
            x = 10
            if x1 + x > 900:
                x = 900 - x2                                        #boucle permettant de ramener à x2 = 900 si x2 dépasse à droite
            self.canvas.move(self.raquette, x, 0)