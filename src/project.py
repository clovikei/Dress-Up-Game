import pygame
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

def wardrobe(screen, assets, panel):
    pygame.draw.rect(screen, (255, 220, 235), panel, border_radius=16)
    pygame.draw.rect(screen, (200, 150, 170), panel, width=2, border_radius=16)

def main():
    pygame.init()
    pygame.display.set_caption("Dress-Up Game")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    assets = import_assets()
    panel = pygame.Rect(540, 30, 230, 540)
    character = assets["character"]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 240, 248))
        screen.blit(character, (125, 75))
        clothing_panel = wardrobe(screen, assets, panel)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()



if __name__ == "__main__":
    main()