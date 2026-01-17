import pygame
from sys import exit
from math import sqrt
import random

class PhysicsEngine:
    def __init__(self):
        pygame.init()
        self.time_frame = 1/60
        self.width = 800
        self.height = 650
        self.gravity = 9.81 * self.time_frame
        self.balls = []
        self.clock = pygame.time.Clock()
        self.colors = ['red', 'blue', 'orange', 'yellow', 'white', 'purple']

        self.keys = pygame.key.get_pressed()
        self.release_pos = None
        self.click_pos = None


        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Physics Engine with BALLS!')
    
    def add_ball(self, position, velocity=(0,0)):
        ball = {
            'pos': list(position),
            'velocity': list(velocity),
            'color': self.colors[random.randint(0, len(self.colors) - 1)],
            'radius': random.randint(7, 15)
        }
        self.balls.append(ball)

    def collisions(self):
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball1 = self.balls[i]
                ball2 = self.balls[j]

    
    def update(self):
        for ball in self.balls:
            ball['velocity'][1] += self.gravity
            ball['pos'][1] += ball['velocity'][1]
            ball['pos'][0] += ball['velocity'][0]

            if ball['pos'][1] + ball['radius'] >= self.height:
                ball['pos'][1] = self.height - ball['radius']
                ball['velocity'][1] = -ball['velocity'][1] * 0.7
            
            if ball['pos'][0] + ball['radius'] >= self.width:
                ball['pos'][0] = self.width - ball['radius']
                ball['velocity'][0] = -ball['velocity'][0] * 0.7

            if ball['pos'][0] + ball['radius'] <= 0:
                ball['pos'][0] = ball['radius']
                ball['velocity'][0] = -ball['velocity'][0] * 0.7
            
            if ball['pos'][1] + ball['radius'] <= 0:
                ball['pos'][1] = ball['radius']
                ball['velocity'][1] = -ball['velocity'][1] * 0.7
                
    def draw(self):
        self.window.fill((0, 0, 0))
        for ball in self.balls:
            pygame.draw.circle(self.window, ball['color'], (int(ball['pos'][0]), (int(ball['pos'][1]))), ball['radius'])
    
        pygame.display.update()
    
    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_pos = pygame.Vector2(event.pos)
                    print(self.click_pos)
                
                if event.type == pygame.MOUSEBUTTONUP:
                    self.release_pos = pygame.Vector2(event.pos)

                    if self.click_pos:

                        direction = self.release_pos - self.click_pos
                        if self.release_pos != self.click_pos:
                            speed = direction.length() / 10
                            velocity = direction.normalize() * speed
                        else:
                            velocity = (0,0)

                        self.add_ball(self.click_pos, velocity)
                        self.click_pos = None


            self.draw()
            self.update()
            self.clock.tick(60)

if __name__ == '__main__':
    Engine = PhysicsEngine()
    Engine.run()    