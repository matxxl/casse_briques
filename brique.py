class Brique:
    
    def __init__(self, canvas, x, y, width, height, color="#FF0000", hits=1):
        
        self.canvas = canvas          
        self.x = x                    
        self.y = y                    
        self.width = width
        self.height = height
        self.color = color
        self.hits = hits              # Nombre de hits nécessaires pour détruire la brique

        # Crée le rectangle sur le canvas
        self.id = canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height,
            fill=self.color, outline="black"
        )

    def hit(self):
        """Appelé quand la balle touche la brique."""
        self.hits -= 1
        if self.hits <= 0:
            self.destroy()
        else:
            self.update_color()

    def update_color(self):
        """Optionnel : change la couleur selon les hits restants."""
        colors = {1: "red", 2: "orange", 3: "yellow"}
        self.canvas.itemconfig(self.id, fill=colors.get(self.hits, "#848484"))

    def destroy(self):
        """Supprime la brique du canvas."""
        self.canvas.delete(self.id)

    def get_coordonnées(self):
        """Retourne les coordonnées actuelles pour la détection de collision."""
        return self.canvas.coordonnées(self.id)
