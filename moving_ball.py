import pygame
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.height = 600
        self.width = 800
        self.window = pygame.display.set_mode((self.width, self.height))

        self.x = self.width/2
        self.y = self.height/2
        self.radius = 15

        self.timestep = 1/60
        self.gravity = 9.81 * self.timestep

        self.vel_y = 4
        self.vel_x = 0
        self.on_ground = False
        self.speed = 0.8
        self.friction = 0.9
        self.bounce = 0.7

        self.clock = pygame.time.Clock()
    
    def draw(self):
        self.window.fill((0,0,0))
        circle = pygame.draw.circle(self.window, 'red', (self.x, self.y), self.radius)
        pygame.display.update()

    def update(self):
        keys = pygame.key.get_pressed()
        
        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y + self.radius >= self.height:
            self.y = self.height - self.radius
            self.vel_y = -self.vel_y * 0.7
            self.on_ground = True
        else:
            self.on_ground = False
        
        if keys[pygame.K_d]:
            self.vel_x += self.speed
        
        if keys[pygame.K_a]:
            self.vel_x -= self.speed

        if keys[pygame.K_w] and self.on_ground:
            self.vel_y = -10
            self.on_ground = False
        
        if keys[pygame.K_s]:
            self.y += self.vel_y
        
        
        self.x += self.vel_x
        self.vel_x *= self.friction
        
        self.collisions()

    def collisions(self):
        if self.x + self.radius >= self.width:
            self.x = self.width - self.radius
            self.vel_x = - self.vel_x * 0.7
        
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vel_x = - self.vel_x * 0.7
            
        
    
    def run(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()
            
            
            self.draw()
            self.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()