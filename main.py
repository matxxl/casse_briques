import tkinter as tk

class casse_briques:
    def __init__(self, master):
        self.master = master
        master.title("Casse Briques")
        self.canvas = tk.Canvas(master, width = 900, height = 500, bg ='black')
        self.canvas.grid(row = 1, column = 0, columnspan = 3)
        self.label_texte1 = tk.Label(master, text = "Vies :")
        self.label_texte1.grid(row = 0, column = 1, columnspan = 3)
        self.label_texte2 = tk.Label(master, text = "Score : ")
        self.label_texte2.grid(row = 0, column = 0, columnspan = 3)
        self.bouton = tk.Button(master, text = "Quitter", command = root.destroy)
        self.bouton.grid(row = 2, column = 1)

'''    def __objet__(self):
        self.brique = tk.create_rectangle(width = 90, height = 30, bg = 'green')'''
 


if __name__ == "__main__" :
    root =tk.Tk()
    app = casse_briques(root)
    root.mainloop()