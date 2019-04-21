from Sprite import Sprite
from Bullet import Bullet
from Player import Player
from Shooter import Shooter
import SpriteManager

class SlimeBaby (Sprite):
    
    diameter = 40
    c = color(127,250,0)
    speed = 0.8
    
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
