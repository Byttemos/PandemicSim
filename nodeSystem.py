import numpy as np
import pygame, sys
import pandas as pd

class NodeSystem:
    def __init__(self, screen, n):
        self.screen = screen
        self.nodes = np.zeros((n, 5))
        self.nodes[:, [0, 1]] = np.random.randint([self.screen.get_width(), self.screen.get_height()], size = (n, 2)) #Initial position of the nodes, with the screensize as boundaries.
        self.nodes[:, [3, 4]] = np.random.rand(n, 2)*2-1 #Node velocity
        self.sick_color = 255, 0, 0
        self.healthy_color = 0, 255, 0
        self.innoculated = 0, 0, 255
        self.immune = 125, 0, 125

        self.node_radius = 2 #Radius of Nodes (GIRTH)

    """Deprecated function. rewrite"""
    def color(self, row):
        if not row[2]:
           return self.healthy_color
        else:
           return self.sick_color


    def addNode(self, coords = None):
        coords = coords if coords else np.random.randint([self.screen.get_width(), self.screen.get_height()])#chris forklarer det her shit når han kommer hjem
        row = np.array([*coords, 0, 1])
        print(self.nodes.shape, row.shape)
        self.nodes = np.vstack((self.nodes, row))


    def logData(self, data):
        print(data.shape)
        print(self.nodes.shape)
        np.concatenate((data, self.nodes))




    def drawNodes(self):

        for row in self.nodes:
            pygame.draw.circle(self.screen, self.color(row), row[[0,1]], self.node_radius, 0)

    """Update position and reverse direction for all nodes with coordinates out of bounds"""
    def updatePosition(self):
        self.nodes[:, [0,1]] += self.nodes[:, [3,4]] #increment position with speed values
        self.nodes[self.nodes[:, 0] < 0, 3] *= (-1)
        self.nodes[self.nodes[:, 0] > self.screen.get_width(), 3] *= (-1)
        self.nodes[self.nodes[:, 1] < 0, 4] *= (-1)
        self.nodes[self.nodes[:, 1] > self.screen.get_height(), 4] *= (-1)
