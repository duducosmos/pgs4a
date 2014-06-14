'''
Created on Apr 1, 2013

@author: redw0lf
'''

from breakout.data.GameElement import GameElement

class Block(GameElement):
    """
    This describes a Block of the breakout game
    """


    def __init__(self, (centerX, centerY)):
        """
        Constructor
        """
        GameElement.__init__(self)
        self.image, self.rect = self.load_image('nicubunu_Banana.png', -1)
        self.hp = 1
        self.rect.center = (centerX, centerY)
        
        
        
        
    def decreaseHP(self):
        self.hp = self.hp - 1
        return self.hp    
    def setCenter(self, (centerX, centerY)):
        self.rect.center = (centerX, centerY)
                
