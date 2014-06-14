'''
Created on Apr 1, 2013

@author: redw0lf
'''
import pygame


from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION
from breakout.data.GameElement import GameElement


class Ball(GameElement):
    """
    This class describes the game ball, which moves around the screen
    with a given slope and a given speed
    """
    def __init__(self):
        # GameElement.__init__(self)
        GameElement.__init__(self)
        self.image, self.rect = self.load_image('nicubunu_Monkey_head.png', -1)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        
        self.slope = 3
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.speed = -3
        self.rect.center = self.area.center
        self.rect.y = self.area.height - 2 * self.rect.h
        self.resetState = True
        

    def update(self):
        """
        this is the update method for the ball, it checks
        if the ball is within the boundaries of the gamefield
        if this is not the case it is reflected.
        """
        
        # if the ball does not move i.e. in the beginning and after
        # a reset the update step is skipped
        if self.resetState == True:
            return       

        #lets the ball reflect from the walls
        if self.rect.top < self.area.top or \
           self.rect.bottom > self.area.bottom:
            self.slope = -self.slope
            
        if self.rect.left < self.area.left or \
           self.rect.right > self.area.right:
            self.speed = -self.speed

        newpos = self.rect.move((self.speed, self.slope))
        self.rect = newpos
 
            
            
    def checkHit(self, targets):
        """ 
        Checks for multiple Blocks, if the ball collides with
        any of these blocks
        """
        for target in targets.sprites():
            

            hitbox = target.rect
            if hitbox.colliderect(self.rect):
                # check if hit from side, this is when the center of the ball
                # is within the top and bottom of the block
                #hitbox = target.rect.inflate(0, 0)
                if self.rect.centery < hitbox.top and \
                self.rect.centery > hitbox.bottom:
                    self.speed = -self.speed
                else:
                    self.slope = -self.slope    
                
                return target
        return None
    
    def handleEvent(self, event):
        """
        Event handler for the ball
        if the ball is in the reset state it moves according to the mouse
        if the mousebutton is clicked the reset state is leaved
        """
        if event.type == MOUSEMOTION:
            if self.resetState == True:
                
                self.rect.center = (event.pos[0], self.rect.centery)
        elif event.type == MOUSEBUTTONDOWN:
            self.resetState = False
            
            
    def reverse(self):
        self.slope = -self.slope
       
    def reflect(self):
        self.speed = -self.speed

    def resetSelf(self, barPosition):
        """
        sets the ball on top of the bar and let the ball
        enter the reset state
        """
        self.rect.centerx = barPosition.centerx
        self.rect.midbottom = barPosition.midtop
        self.resetState = True
        
