import tkinter as tk

class Raquette:
    def __objet__(self):
                root = tk.Tk()
                root.title('raquette')
                self.raquette = tk.Canvas.create_rectangle(root, width = 50, height = 20)
                root.mainloop()

app = Raquette()