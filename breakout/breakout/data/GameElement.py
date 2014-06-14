'''
Created on Apr 1, 2013

@author: redw0lf
'''
import os
import pygame
from pygame.locals import RLEACCEL 

class GameElement(pygame.sprite.Sprite):
    """
    the basic GameElement class all other game elements
    are derived from this class. hence this class has the
    load_image method
    """


    def __init__(self):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        
    def load_image(self, name, colorkey=None):
        fullname = os.path.join('./data', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', fullname
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image, image.get_rect()
        
