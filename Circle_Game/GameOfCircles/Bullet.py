from Sprite import Sprite

class Bullet(Sprite):
    
    diameter = 10
    c = color(0)
    
    def __init__(self, x, y, vector, team):
        self.x = x
        self.y = y
        self.vector = vector
        self.team = team
        
    def move(self):
        self.x += self.vector.x
        self.y += self.vector.y
        
