import pygame
import os
import sys

def import_assets():
    #base character
    base_character = pygame.image.load("assets/oguri.png").convert_alpha()
    return base_character

def main():
    pygame.init()
    pygame.display.set_caption("Dress-Up Game")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    character = import_assets()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('Black')
        pygame.display.flip()
    pygame.quit()

#TODO: Import assets, clickable UI, sounds
#character name is oguri


#def function_2():


#def function_n():


if __name__ == "__main__":
    main()