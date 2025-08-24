
#? Importing necessary modules.
import math
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planetary Simulation")
clock = pygame.time.Clock()

#* Defining gravitational constant
G = 6.67430e-11

#* Constants for simulation and visualization:
SCALE = 6e-11
ZOOM_SCALE = 1e-9
DT = 86400

#* To control whether we're zoomed in or not:
zoomed = False

#* Central class for creating planets their masses, sizes, velocity,etc.
class Body():
    # Function which takes: planet's x position, y position, velocity while going in x direction, velocity going in y direction,
    # mass, radius and color of the planet as well.
    def __init__(self, x, y, vx, vy, mass, radius, color):
        self.x = x
        self.y = y 
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.radius = radius
        self.color = color
        self.trail = []  # to keep track of the path that the body is traversing at.

    #* Function for updating positions
    # The parameter bodies: list of celestial bodies in the simulation. 
    # NOTE: The velocities and change in velocities is going to be determined by other bodies.
    def updatePosition(self, bodies): # This is going to be our physics simulation.
        fx = fy = 0  # forces acting on the body initially set to 0.

        #* Iterating over the list of bodies:
        for other in bodies:
            if other is self:
                continue
            dx = other.x - self.x  # distance in x direction.
            dy = other.y - self.y  # distance in y direction.
            r = math.sqrt(dx ** 2 + dy ** 2) # to calculate the euclidean distance.
            if r > 0:
                # F = G * (m1 * m2) / r^2
                f = G * self.mass * other.mass / (r ** 2)
                fx += f * dx / r
                fy += f * dy / r
        
        # F = ma   ->    a = F / m
        ax = fx / self.mass 
        ay = fy / self.mass
        self.vx += ax * DT
        self.vy += ay * DT
        self.x += self.vx * DT
        self.y += self.vy * DT

        current_scale = ZOOM_SCALE if zoomed else SCALE

        screen_x = int(self.x * current_scale + WIDTH // 2)
        screen_y = int(self.y * current_scale + HEIGHT // 2)
        self.trail.append((screen_x, screen_y))
        if len(self.trail) > 200:
            self.trail.pop(0)        

        
    def draw(self, screen):
        if len(self.trail) > 1:
            pygame.draw.lines(screen, (50, 50, 50), False, self.trail, 1)
        
        current_scale = ZOOM_SCALE if zoomed else SCALE

        screen_x = int(self.x * current_scale + WIDTH // 2)
        screen_y = int(self.y * current_scale + HEIGHT // 2)

        pygame.draw.circle(screen, self.color, (screen_x, screen_y), self.radius)

bodies = [
    # Sun -> (1.989e30 kg, 8 pixel radius (not used in calculations, just visual))
    Body(0, 0, 0, 0, 1.9899e30, 8, (255, 255, 0)),
    Body(5.79e10, 0, 0, 47360, 3.301e23, 2, (169, 169, 169)),  # Mercury
    Body(1.082e11, 0, 0, 35020, 4.867e24, 3, (255, 165, 0)),  # Venus
    Body(1.496e11, 0, 0, 29780, 5.972e24, 4, (0, 100, 255)),  # Earth
    Body(2.79e11, 0, 0, 24077, 6.39e23, 3, (255, 100, 0)),  # Mars (fixed magnitude formatting)
    Body(7.786e11, 0, 0, 13070, 1.898e27, 6, (200, 150, 100)),  # Jupiter
    Body(1.432e12, 0, 0, 9680, 5.683e26, 5, (250, 200, 100)),  # Saturn
    Body(2.867e12, 0, 0, 6810, 8.681e25, 4, (100, 200, 255)),  # Uranus
    Body(4.515e12, 0, 0, 5430, 1.024e26, 4, (0, 0, 255)),  # Neptune
    Body(5.906e12, 0, 0, 4670, 1.309e22, 2, (150, 100, 50)),  # Pluto
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                zoomed = not zoomed
                for body in bodies:
                    body.trail = []
            
    screen.fill((0, 0, 0))

    for body in bodies:
        body.updatePosition(bodies)
        body.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()