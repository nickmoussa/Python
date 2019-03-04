import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from RainDrop import RainDrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Bullet import Bullet

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(ScreenSaverBot(100, 50, 2))
    SpriteManager.spawn(RainDrop(100, 60, 2))
    SpriteManager.spawn(RainDrop(350, 60, 2))
    
                           
def draw():
    global player, sprites
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()   
        
def keyReleased():
    SpriteManager.player.keyUp()
