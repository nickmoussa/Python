from Sprite import Sprite
from Bullet import Bullet
from Player import Player
from Shooter import Shooter
import SpriteManager

class ArmoredShooter(Shooter, Sprite):
    armor = 7
    
    def display(self):
        stroke(100)
        strokeWeight(self.armor)
        fill(255, 0, 0)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
        
    def handleCollision(self):
        self.armor -= 1
        if self.armor < 0:
            SpriteManager.destroy(self)    
    

        
