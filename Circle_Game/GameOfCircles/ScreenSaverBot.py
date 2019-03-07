from Sprite import Sprite
from Bullet import Bullet
class ScreenSaverBot(Sprite):
    
    xspeed = 6
    yspeed = 4
    diameter = 50
    c = color(0,150,100)
    
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0 or self.y > height:
            self.yspeed *= -1        
        
    
