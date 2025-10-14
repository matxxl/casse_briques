from tkinter import *

class Raquette:
    def __init__(self, canvas):
        self.x = 450
        self.y = 400
        self.canvas = canvas
        self.raquette = canvas.create_rectangle(self.x, self.y, self.x + 100, self.y +15, fill = 'orange')
    
    def déplacer_gauche(self, event):
        x = -10
        y=0
        self.canvas.move(self.raquette, x, y)
    
    def déplacer_droite(self, event):
        x = 10
        y = 0
        self.canvas.move(self.raquette, x, y)