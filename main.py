import tkinter as tk
import raquette as rq

class Casse_briques:
    def __init__(self):
        root = tk.Tk()
        root.title("Casse Briques")
        self.canvas = tk.Canvas(root, width = 900, height = 500, bg ='black')
        self.canvas.grid(row = 1, column = 0, columnspan = 3)
        self.label_texte1 = tk.Label(root, text = "Vies :")
        self.label_texte1.grid(row = 0, column = 1, columnspan = 3)
        self.label_texte2 = tk.Label(root, text = "Score : ")
        self.label_texte2.grid(row = 0, column = 0, columnspan = 3)
        self.bouton = tk.Button(root, text = "Quitter", command = root.destroy)
        self.bouton.grid(row = 2, column = 1)
        self.raquette = rq.Raquette(self.canvas)
        root.bind("<Left>", self.raquette.left1)
        root.bind("<Right>", self.raquette.right1)
        root.mainloop()

 
if __name__ == "__main__" :
    app = Casse_briques()