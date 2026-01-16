import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

def planet():
    def __init__(self):
        pass

def main():
    run = True
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()

    
    while run:
        clock.tick(60)
        window.fill('red')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


main()