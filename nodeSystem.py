import numpy as np
import pygame, sys


class NodeSystem:
    def __init__(self, screen, n):
        self.screen = screen
        self.nodes = np.zeros((n, 5))
        self.nodes[:, [0, 1]] = np.random.randint([self.screen.get_width(), self.screen.get_height()], size = (n, 2))
        self.nodes[:, [3, 4]] = np.random.rand(n, 2)*2-1
        self.sick_color = 255, 0, 0
        self.healthy_color = 0, 255, 0
        self.node_radius = 2

    def color(self, row):
        if not row[2]:
           return self.healthy_color
        else:
           return self.sick_color



    def addNode(self, coords = None):
        coords = coords if coords else np.random.randint([self.screen.get_width(), self.screen.get_height()])
        row = np.array([*coords, 0, 1])
        print(self.nodes.shape, row.shape)
        self.nodes = np.vstack((self.nodes, row))


    def logData(self, data):
        return np.concatenate((data, self.nodes))




    def drawNodes(self):

        for row in self.nodes:
            pygame.draw.circle(self.screen, self.color(row), row[[0,1]], self.node_radius, 0)

    """Update position and reverse direction for all nodes with coordinates out of bounds"""
    def updatePosition(self):
        self.nodes[:, [0,1]] += self.nodes[:, [3,4]]
        self.nodes[self.nodes[:, 0] < 0, 3] *= (-1)
        self.nodes[self.nodes[:, 0] > self.screen.get_width(), 3] *= (-1)
        self.nodes[self.nodes[:, 1] < 0, 4] *= (-1)
        self.nodes[self.nodes[:, 1] > self.screen.get_height(), 4] *= (-1)
