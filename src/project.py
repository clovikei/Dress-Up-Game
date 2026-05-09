import pygame
import os

def main():
    pygame.init()
    pygame.display.set_caption("Dress-Up Game")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('Black')
        pygame.display.flip()
    pygame.quit()

#def function_1():


#def function_2():


#def function_n():


if __name__ == "__main__":
    main()