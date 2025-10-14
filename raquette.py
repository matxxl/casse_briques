from tkinter import *

class Raquette:
    def __init__(self, canvas):
        self.x = 450
        self.y = 400
        self.canvas = canvas
        self.raquette = canvas.create_rectangle(self.x, self.y, self.x + 100, self.y +15, fill = 'orange')
    
    def left(self, event):
        x = -10
        y=0
        self.canvas.move(self.raquette, x, y)
    
    def right(self, event):
        x = 10
        y = 0
        self.canvas.move(self.raquette, x, y)

    def left1(self, event):
        x1,y1,x2,y2 = self.canvas.coords(self.raquette)
        if x1 > 0:
            x = -10
            if x1 + x <0:
                x = -x1
            self.canvas.move(self.raquette, x, 0)

    def right1(self, event):
        x1,y1,x2,y2 = self.canvas.coords(self.raquette)
        if x2 < 900:
            x = 10
            if x1 + x > 900:
                x = 900 - x2
            self.canvas.move(self.raquette, x, 0)