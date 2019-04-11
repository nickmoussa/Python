from Sprite import Sprite
from Bullet import Bullet
from Player import Player
from Shooter import Shooter
import SpriteManager

class SlimeBot(Sprite):
    
    
    diameter = 100
    c = color(127,250,0)
    angle = 0.02
    xspeed = 2
    yspeed = 2
        
    def move(self):
        
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            self.xspeed *= -1
            self.yspeed *= -1
        
        self.angle += 0.02
    
        self.x += (2*sin(self.angle))
        
        self.y += self.yspeed
        
