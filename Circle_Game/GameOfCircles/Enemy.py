from Sprite import Sprite
from Bullet import Bullet
from Player import Player
from Shooter import Shooter

import SpriteManager

class Enemy(Shooter, Sprite):
    
    speed = 8
    diameter = 50
    c = color(0, 0, 255)
    
    def move(self):
        Shooter.move(self)
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        
        
               
