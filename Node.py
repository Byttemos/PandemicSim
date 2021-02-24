import numpy as np
import pygame
class Node:
    """ Constructor. instantiate n nodes with speed, position and contagion status """
    def __init__(self, screen, status=1, radius=20):
        self.healthy_color = 0, 255, 0
        self.sick_color = 255, 0, 0
        self.speed = np.random.rand(2)
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.pos = np.array([np.random.randint(self.width), np.random.randint(self.height)]).astype(float)
        self.status = status
        self.radius = radius

    @property
    def color(self):
        return self.healthy_color if self.status == 1 else self.sick_color

    def makeSick(self):
        self.status = 0

    def makeHealthy(self):
        self.status = 1

    def update(self):
        self.pos += self.speed
        self.checkBounds()


    def checkBounds(self):
        if self.pos[0] + 4 > self.width or self.pos[0] < 4:
            self.speed[0] = -self.speed[0]

        if self.pos[1] +4 > self.height or self.pos[1] < 4:
            self.speed[1] = -self.speed[1]
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius, 0)

    def spreadInfection(self, node):
        distvec = self.pos - node.pos
        dist = np.sqrt(distvec[0]**2+distvec[1]**2)
        if dist < self.radius:
            if not self.status:
                node.makeSick()
            if not node.status:
                self.makeSick()
