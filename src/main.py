
#* Importing necessary modules.
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
            if other != self:
                dx = other.x - self.x  # distance in x direction.
                dy = other.y - self.y  # distance in x direction.
                r = math.sqrt(dx ** 2 + dy ** 2) # to calculate the eucledian distance.
                if r > 0:
                    f = G * self.mass * other.mass /(r*2)
        

