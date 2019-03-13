from Sprite import Sprite
from Bullet import Bullet
from Player import Player
from Shooter import Shooter
import SpriteManager

class ArmoredShooter(Shooter, Sprite):
    
    speed = 4
    diameter = 50
    c = color(0,0,0)
    ArmorThickness = 10
    
    def display(self):
        fill(self.c)
        stroke(0)
        strokeWeight(self.ArmorThickness)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
    
    def move(self):
        Shooter.move(self)
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
    def ArmorSkin(self):
        strokeWeight(50)
        
               
