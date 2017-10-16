import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")


class SnowFlake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''

    def __init__(self, size, position, wind):
        self.size = size
        self.position = position
        self.wind = wind
    
    
    def fall(self, speed):
        self.position[1]+=speed
        '''
        Take in a int that represnts the speed at which the snowflake is falling in the y-direction.  
        A + int will have the snowflake falling down the screen. 
        A - int will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
        '''
        wind = False
    def draw(self):
       
        '''
        Uses pygame and the global screen variable to draw the snowflake on the screen
        '''
        pygame.draw.circle(screen, WHITE, self.position, self.size)

		
	# ---- end of class is here!	

	
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Speed
speed = 1


# Snow List - it's empty in the beginning! You must initialize
# snowflakes objects in the code below.
snow_list = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    # Begin Snow

	#call or make the object place into a list
    x = random.randrange(0, 700)
    y = 0
    snow_list.append(SnowFlake(2, [x,y], True))
	#call the fall function on that objectmySnowflake
    for snowflake in snow_list:
        snowflake.draw()
        snowflake.draw()
        snowflake.fall(speed)
	

    # End Snow
    # --- update screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
