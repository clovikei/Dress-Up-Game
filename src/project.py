import pygame
import os
import sys

def import_assets():

    base_character = pygame.image.load("assets/oguri.png").convert_alpha()

    hats = [
        pygame.image.load("assets/sporty_hat.png").convert_alpha(),
        pygame.image.load("assets/kiryu_hat.png").convert_alpha(),
        pygame.image.load("assets/jirai_hat.png").convert_alpha(),
        pygame.image.load("assets/cute_hat.png").convert_alpha(),
        pygame.image.load("assets/cool_hat.png").convert_alpha()
    ]

    tops = [
        pygame.image.load("assets/sporty_top.png").convert_alpha(),
        pygame.image.load("assets/kiryu_top.png").convert_alpha(),
        pygame.image.load("assets/jirai_top.png").convert_alpha(),
        pygame.image.load("assets/cute_top.png").convert_alpha(),
        pygame.image.load("assets/cool_top.png").convert_alpha()
    ]

    bottoms = [
        pygame.image.load("assets/sporty_bottom.png").convert_alpha(),
        pygame.image.load("assets/kiryu_bottom.png").convert_alpha(),
        pygame.image.load("assets/jirai_bottom.png").convert_alpha(),
        pygame.image.load("assets/cute_bottom.png").convert_alpha(),
        pygame.image.load("assets/cool_bottom.png").convert_alpha()
    ]
    return {
        "character": base_character,
        "hats": hats,
        "tops": tops,
        "bottoms": bottoms
    }

def main():
    pygame.init()
    pygame.display.set_caption("Dress-Up Game")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    assets = import_assets()
    character = assets["character"]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('Green')
        screen.blit(character, (250, 50))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

#TODO: Import assets, clickable UI, sounds
#character name is oguri


#def function_2():


#def function_n():


if __name__ == "__main__":
    main()