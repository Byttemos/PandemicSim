import numpy as np
import pygame
class Node:

    """ Constructor. instantiate nodes with various attributes """
    def __init__(self, screen, status=1, radius=5):
        self.healthy_color = 0, 255, 0
        self.sick_color = 255, 0, 0
        self.speed = np.random.rand(2)*2-1
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.pos = np.array([np.random.randint(self.width), np.random.randint(self.height)]).astype(float)
        self.status = status
        self.radius = radius

    """Decorator function. @property gives the color function setter functionality"""
    @property
    def color(self):
        return self.healthy_color if self.status == 1 else self.sick_color

    """Make target node sick"""
    def makeSick(self):
        self.status = 0



    """Make target node healthy"""
    def makeHealthy(self):
        self.status = 1

    """Increment node position and serve as wrapper function for checkBounds"""
    def update(self):
        self.pos += self.speed
        self.checkBounds()


    """Check if node is out of bounds and reverse their direction if so"""
    def checkBounds(self):
        if self.pos[0] + 4 > self.width or self.pos[0] < 4:
            self.speed[0] = -self.speed[0]

        if self.pos[1] +4 > self.height or self.pos[1] < 4:
            self.speed[1] = -self.speed[1]

    """Draw a node on the screen"""
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, 0)

    """Collision detection and contagion"""
    def spreadInfection(self, node):
        distvec = self.pos - node.pos
        dist = np.sqrt(distvec[0]**2+distvec[1]**2)
        if dist < self.radius:
            if not self.status:
                node.makeSick()
            if not node.status:
                self.makeSick()

