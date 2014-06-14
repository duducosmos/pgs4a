'''
Created on Mar 25, 2013

@author: redw0lf
'''
import pygame, sys, os, random
from pygame.locals import * 
from breakout.data.Ball import Ball
from breakout.data.Bar import Bar
from breakout.data.Block import Block


# Import the android module. If we can't import it, set it to None - this
# lets us test it, and check to see if we want android-specific behavior.
try:
    import android
except ImportError:
    android = None


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
# Initialize Everything
    width = 800
    height = 600
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('break0ut')
    pygame.mouse.set_visible(0)
    
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    
    # Map the back button to the escape key.
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
    
    # Display The Background
    #  screen.blit(background, (0, 0))
    #    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()

    # create the bar and set the y position of the bar
    gameBar = Bar(screen.get_height() - 50)
    
    playBall = Ball()
    
    playBall.resetSelf(gameBar.rect)
    
    moveableSprites = pygame.sprite.RenderPlain((gameBar, playBall))
    
    # sample Block
    aBlock = Block((10, 10))
    
    #create a pit bottom for the ball, which is used to reset the ball
    pitBottom = Rect(0, height - 10, width, 10)
    
    #block area should occupy 80% of the width and 50% of height
    blockAreaWidth = int(width * 0.8)
    blockAreaHeight = int(height * 0.5)
    
    maxBlockInX = int(blockAreaWidth/aBlock.rect.width)
    
    #update the block area width to the correct size
    blockAreaWidth = (maxBlockInX*aBlock.rect.width)
    
    # get start position for x
    blockStartX = int((width - (blockAreaWidth)) / 2)
    blockStartY = int(blockStartX) # same difference above as on the sides
    
    
    # create the blocks start at the x value and go until the max width has reached
    # there should be no space between the current and the next block
    gameAreaSprites = pygame.sprite.RenderPlain()
    for blockPosX in xrange(blockStartX, (width - blockStartX), aBlock.rect.w):
        for blockPosY in xrange(blockStartY, (blockAreaHeight + blockStartY), aBlock.rect.h):
            gameAreaSprites.add(Block((blockPosX, blockPosY)))
    

    # draw background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
   
    # main game loop
    while 1:
        clock.tick(60)
        
        # Android-specific:
        if android:
            if android.check_pause():
                android.wait_for_resume()

        # Handle Input Events
        for event in pygame.event.get():
            # quit the game if escape is pressed
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            # move the handles according to the object
            elif event.type == MOUSEMOTION:
                gameBar.handleEvent(event)
                playBall.handleEvent(event)
            elif event.type == MOUSEBUTTONDOWN:
                playBall.handleEvent(event)
        
        
        # check if a block has hit a ball, if so remove the block
        # the ball is reversed in the checkhit method   
        hit = playBall.checkHit(gameAreaSprites)    
        if hit:
            if hit.decreaseHP() == 0:
                gameAreaSprites.remove(hit)
            
        gameBar.checkBarHit(playBall)
        
        if pitBottom.colliderect(playBall.rect):
            playBall.resetSelf(gameBar.rect)
        
   

    # update and draw Everything
        gameAreaSprites.update()
        moveableSprites.update()
        screen.blit(background, (0, 0))
        moveableSprites.draw(screen)
        gameAreaSprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()
