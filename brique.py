class Brique :
    
    couleur_brique = "blue"
    
    def __init__(self, x, y, hits):
        self.width = 75
        self.height = 20
        self.position = PVecteur(x, y)
        self.hits = hits
        self.couleur = Brique.couleur_brique

    def display(self):
        fill(self.couleur)
        stroke("black")
        strokeWeight(2)
        rect(self.position.x, self.position.y, self.width, self.height)
        