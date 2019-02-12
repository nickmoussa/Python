import platform
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from RainDrop import RainDrop
from SpriteManager import sprites
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    
    sprites.append(player)
    sprites.append(Enemy(50, 50, enemyTeam))
    sprites.append(Enemy(70, 150, enemyTeam))
    sprites.append(RainDrop(70, 70, enemyTeam))
    sprites.append(RainDrop(90, 80, enemyTeam))
    sprites.append(RainDrop(400, 90, enemyTeam))
    sprites.append(RainDrop(340, 100, enemyTeam))
    sprites.append(RainDrop(390, 110, enemyTeam))
    sprites.append(RainDrop(400, 120, enemyTeam))
    sprites.append(RainDrop(380, 130, enemyTeam))
    sprites.append(RainDrop(370, 200, enemyTeam))
    sprites.append(RainDrop(330, 60, enemyTeam))
    sprites.append(RainDrop(350, 40, enemyTeam))
    sprites.append(JiggleBot(100, 100, enemyTeam))
    sprites.append(ScreenSaverBot(100, 100, enemyTeam))
                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
