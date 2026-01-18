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
            'radius': random.randint(15, 20)
        }
        self.balls.append(ball)

    def collisions(self):
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                ball1 = self.balls[i]
                ball2 = self.balls[j]
            
                dx = ball1['pos'][0] - ball2['pos'][0]
                dy = ball1['pos'][1] - ball2['pos'][1]
                distance = sqrt(dx**2 + dy**2)

                if distance < ball1['radius'] + ball2['radius']:
                    nx = dx / distance
                    ny = dy / distance

                    tx = -ny
                    ty = nx

                    Tan1 = tx * ball1['velocity'][0] + ty * ball1['velocity'][1]
                    Tan2 = tx * ball2['velocity'][0] + ty * ball2['velocity'][1]

                    Norm1 = nx * ball1['velocity'][0] + ny * ball1['velocity'][1]
                    Norm2 = nx * ball2['velocity'][0] + ny * ball2['velocity'][1]

                    m1 = m2 = 1

                    vNorm1 = (Norm1 * (m1 - m2) + 2 * m2 * Norm1) / (m1 + m2)
                    vNorm2 = (Norm2 * (m2 - m1) + 2 * m1 * Norm2) / (m1 + m2)

                    ball1['velocity'][0] = tx * Tan1 + nx * vNorm1
                    ball1['velocity'][1] = ty * Tan1 + ny * vNorm1
                    ball2['velocity'][0] = tx * Tan2 + nx * vNorm2
                    ball2['velocity'][1] = ty * Tan2 + ny * vNorm2

                    overlap = ball1['radius'] + ball2['radius'] - distance
                    ball1['pos'][0] += nx * overlap / 2
                    ball1['pos'][1] += ny * overlap / 2
                    ball2['pos'][0] -= nx * overlap / 2
                    ball2['pos'][1] -= ny * overlap / 2
                    
    
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
            
            self.collisions()
                
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