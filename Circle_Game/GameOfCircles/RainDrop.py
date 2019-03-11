from Sprite import Sprite
from Bullet import Bullet
class RainDrop(Sprite):
    
    speed = 5
    diameter = 50
    c = color(0,0,255)
        
    def move(self):
        self.y += self.speed
        if self.y < 0 :
            self.speed *= -1
        if self.y > width:
            self.y = 0    
