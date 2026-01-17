import pygame
from sys import exit
from math import sqrt

class PhysicsEngine:
    def __init__(self):
        pygame.init()
        self.radius = 10
        self.color = 'blue'
        self.width = 800
        self.height = 650
        self.gravity = 9.81
        self.balls = []
        clock = pygame.time.Clock()
        clock.tick(60)

        self.keys = pygame.key.get_pressed()
        
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Physics Engine with BALLS!')
    
    def ball(self):
        pass
    
    def draw(self):
        pygame.draw.circle(self.window, self.color, (100, 100), self.radius)
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()

            self.draw()

if __name__ == '__main__':
    Engine = PhysicsEngine()
    Engine.run()    