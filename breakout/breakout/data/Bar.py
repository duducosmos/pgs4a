'''
Created on Apr 1, 2013

@author: redw0lf
'''

import pygame
from pygame.locals import MOUSEMOTION 
from breakout.data.GameElement import GameElement


class Bar(GameElement):
    '''
    This is the Bar class, basically this is the player,
    which is capable of moving the bar and firing the ball if it is lost
    '''
    def __init__(self, yPos):
        GameElement.__init__(self)
        self.image, self.rect = self.load_image('fist.bmp', -1)
        screen = pygame.display.get_surface()
        
        self.yPos = yPos
        self.area = screen.get_rect()
        
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centery = self.yPos
        self.rect.centerx = self.area.centerx
        
        
        
    def handleEvent(self, event):
        """
        handles an event for the bar in this case only the
        mousemotion is handled, which is used to position the bar
        """
        if event.type == MOUSEMOTION:
            pos = event.pos
            self.rect.center = (pos[0], self.yPos)


    def checkBarHit(self, ball):
        """
        checks if the bar is hit by the ball
        if so reverse the ball if the top is hit
        else reflect the ball to drop it in the pit
        """
        hitbox = ball.rect.inflate(-2, -2)
        if hitbox.colliderect(self.rect):
            if self.rect.centery < hitbox.top and \
                self.rect.centery > hitbox.bottom:
                ball.reflect()
            else:
                ball.reverse()
