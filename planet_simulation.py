import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

class Planet:
    AU = 149.6e6 * 1000 # Astronautical Units: Earth distance from sun converted to meters
    G = 6.67428e-11 # Gravitational Constant
    SCALE = 250 / AU # 1AU = 100 px
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2 
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) >= 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
        
            pygame.draw.lines(window, 'white', False, updated_points, 2)

        pygame.draw.circle(window, self.color, (x, y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)\
        
        if other.sun:
            self.distance_to_sun = distance
        
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update(self, planets, timestep):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx / self.mass * timestep
        self.y_vel += total_fy / self.mass * timestep

        self.x += self.x_vel * timestep
        self.y += self.y_vel * timestep

        self.orbit.append((self.x, self.y))

def multiply_mass():
    planets = ['sun', 'earth', 'mars', 'mercury', 'venus']
    multiplier = {}
    while True:
        try:
            for planet in planets:
                value = float(input(f"Multiply {planet}'s Mass By:"))
                multiplier[planet] = value * 0.5
        except ValueError:
            print("Please Enter a Number")
        return multiplier

def time_step():
    while True:
        try:
            days_per_frame = float(input("Days Per Frame:"))
            return days_per_frame
        except ValueError:
            print("Please Print a Value")


def main():
    run = True
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()
    
    multiplier = multiply_mass()
    
    days_per_frame = time_step()
    TIMESTEP = 3600 * 24 * days_per_frame  # 1 day = 86400 seconds


    sun_mass = 1.98892 * 10 ** (30 + multiplier["sun"])
    sun = Planet(0, 0, 30, 'yellow', sun_mass)
    sun.sun = True

    earth_mass = 5.97 * 10 ** (24 + multiplier['earth'])
    earth = Planet(-1 * Planet.AU, 0, 16, 'blue', earth_mass)
    earth.y_vel = 29.783 * 1000
    
    venus_mass = 3.285 * 10 ** (23 + multiplier['venus'])
    venus = Planet(0.723 * Planet.AU, 0, 14, 'orange', venus_mass)
    venus.y_vel = -35.02 * 1000

    mercury_mass = 3.285 * 10 ** (23 + multiplier['mercury'])
    mercury = Planet(0.387 * Planet.AU, 0, 8, 'white', venus_mass)
    mercury.y_vel = -47.4 * 1000

    mars_mass = 6.39 * 10 * (23 + multiplier['mars'])
    mars = Planet(-1.524 * Planet.AU, 0, 12, 'red', mars_mass)
    mars.y_vel = 24.077 * 1000

    planets = [sun, earth, mercury, venus, mars]

    

    while run:
        clock.tick(60)
        window.fill('black')
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        for planet in planets:
            planet.update(planets, TIMESTEP)
            planet.draw(window)
        

        
        pygame.display.update()

    pygame.quit()


main()