import tkinter as tk

class Casse_briques:
    def __init__(self):
        root = tk.Tk()
        root.title("Casse Briques")
        self.canvas = tk.Canvas(root, width = 900, height = 500, bg ='black')
        self.canvas.grid(row = 1, column = 0, columnspan = 3)
        self.label_vies = tk.Label(root, text = "Vies :")
        self.label_vies.grid(row = 0, column = 1, columnspan = 3)
        self.label_score = tk.Label(root, text = "Score : ")
        self.label_score.grid(row = 0, column = 0, columnspan = 3)
        self.bouton = tk.Button(root, text = "Quitter", command = root.destroy)
        self.bouton.grid(row = 2, column = 1)
        root.mainloop()

 
if __name__ == "__main__" :
    app = Casse_briques()
