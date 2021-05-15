import numpy as np
import pygame, sys
from scipy.spatial import distance_matrix

class NodeSystem:
    def __init__(self, n):
        self.nodes = np.zeros((n, 8))
        self.nodes[:, [0, 1]] = np.random.randint([1500, 1000], size = (n, 2))
        self.nodes[:, [2, 3]] = np.random.randn(n, 2)
        self.sick_color = 255, 0, 0
        self.healthy_color = 0, 255, 0
        self.node_radius = 2

    def color(self, row):
        if not row[4]:
           return self.healthy_color
        else:
           return self.sick_color

    def collision_detection(self):
        dm = distance_matrix(self.nodes[:, :2], self.nodes[:, :2])
        self.interact(np.where((dm < self.node_radius*2) & (dm != 0,0)[0]))



    def addNode(self, coords = None):
        """DEPRECATED! add node to node system"""
        coords = coords if coords else np.random.randint([self.screen.get_width(),
                                                          self.screen.get_height()])
        row = np.array([*coords, 0, 1])
        self.nodes = np.vstack((self.nodes, row))


    def logData(self, data):
        """Write data to .npy file"""
        if len(data.shape) == 2:
            return np.stack((data, self.nodes))
        else:
            return np.concatenate((data, self.nodes[None, :, :]))


    def interact(self, node):
        """Determine outcome of a collision between two nodes based on the nodes' properties"""
        for idx in node:
            if self.nodes[node[idx]],4:
                infection_risk = 1



    def infect(node):
        """Spread infection from one node to a collided node. receives sliced array of nodes to be infected"""
        pass


    # def drawNodes(self):

        # for row in self.nodes:
            # pygame.draw.circle(self.screen, self.color(row), row[[0,1]], self.node_radius, 0)


    def updatePosition(self):
        """Increment all node positions and reverse velocity if node is out of bounds"""
        self.nodes[:, [0,1]] += self.nodes[:, [2,3]]
        self.nodes[self.nodes[:, 0] < 0, 2] *= (-1)
        self.nodes[self.nodes[:, 0] > 1500, 2] *= (-1)
        self.nodes[self.nodes[:, 1] < 0, 3] *= (-1)
        self.nodes[self.nodes[:, 1] > 1000, 3] *= (-1)
