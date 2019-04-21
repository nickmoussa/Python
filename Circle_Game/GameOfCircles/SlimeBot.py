from Sprite import Sprite
from Bullet import Bullet
from Player import Player
from Shooter import Shooter
from SlimeBaby import SlimeBaby
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
    
    def handleCollision(self):
        
        SpriteManager.destroy(self)
        for i in range(0,4):
            pos = self.posRandomizer(self.x, self.y)
            SpriteManager.spawn(SlimeBaby(pos.x, pos.y, 2))     

    def posRandomizer(self, x, y):
        t = 115
        return PVector(x + random(-t,t), y + random(-t, t))
