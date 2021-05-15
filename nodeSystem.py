import numpy as np
import pygame, sys
from scipy.spatial import distance_matrix

class NodeSystem:
    def __init__(self, n):
        self.nodes = np.zeros((n, 9))
        self.nodes[:, [0, 1]] = np.random.randint([1500, 1000], size = (n, 2))
        self.nodes[:, [2, 3]] = np.random.randn(n, 2)
        self.healthy_color_mask = 0, 103, 0
        self.healthy_color_no_mask = 0, 255, 0
        self.sick_color_mask = 255, 100, 240
        self.sick_color_no_mask = 150, 0 ,0
        self.vaccinated = 0, 0, 255
        self.immune = 127, 0, 255
        self.dead = 0, 0, 0
        self.node_radius = 2


    def switch_state(self, row):
        """4 = Healthy bool, 5 = Mask bool, 6 = Immune, 7 = Vaccinated, 8 = Dead"""
        states = np.array([4,5,6,7,8])
        find_states = np.where(nodes== 1)
        print(find_states)

        if find_states([8]): #if dead
            dead_x_velocity = [:, 2] = 0
            dead_y_velocity = [:, 3] = 0
            return self.dead

        if find_states([7]): #if vaccinated
            #Do something but don't interact if collision
            return self.vaccinated

        if find_states([6]): #if immune
            #Pause collision contagion for given amount of time
            return self.immune

        if not find_states([4]): #if healthy
            if find_states([5]): #wearing a mask
                return self.healthy_color_mask
            else:  #no mask
                return self.healthy_color_no_mask
        elif find_states([4]): #if sick
            if find_states([5]): #wearing a mask
                return self.sick_color_mask
            else: #no mask
                return self.sick_color_no_mask








            
            
            


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
