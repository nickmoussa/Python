import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from RainDrop import RainDrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
from Bullet import Bullet
from ArmoredShooter import ArmoredShooter
from SlimeBot import SlimeBot

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    size(700, 700)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(SlimeBot(100, 100, 2))
    SpriteManager.spawn(SlimeBot(230, 230, 2))
    SpriteManager.spawn(SlimeBot(580, 400, 2))
    
                           
def draw():
    global player, sprites
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()   
        
def keyReleased():
    SpriteManager.player.keyUp()
