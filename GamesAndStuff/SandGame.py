#This is where the Sand Game will go.
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sand Dropper Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define sand pile class
class SandPile(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Move the sand pile down
        self.rect.y += 1

        # Check if the sand pile has reached the bottom
        if self.rect.bottom >= height:
            # Add the sand pile to the bottom group
            bottom_sand_piles.add(self)
            # Remove the sand pile from the all_sand_piles group
            all_sand_piles.remove(self)

        #Check if the sand pile has collided with any other sand piles
        if pygame.sprite.spritecollide(self, bottom_sand_piles, False):
            #stop the sand pile at the position just above the collision
            self.rect.y -= 1
            #add the sand pile to the bottom group
            bottom_sand_piles.add(self)
            #remove the sand pile from the all_sand_piles group
            all_sand_piles.remove(self)

# Create a group for sand piles
all_sand_piles = pygame.sprite.Group()
bottom_sand_piles = pygame.sprite.Group()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #check if the left mouse button is held down
    if pygame.mouse.get_pressed()[0]:
        #create a sand pile at the mouse positoin
        sand_color = GREEN
        sand_pile = SandPile(sand_color, *pygame.mouse.get_pos())
        all_sand_piles.add(sand_pile)

    # Update
    all_sand_piles.update()

    # Render
    screen.fill(WHITE)
    all_sand_piles.draw(screen)
    bottom_sand_piles.draw(screen)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()