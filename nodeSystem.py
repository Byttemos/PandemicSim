# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:18:39 2021

@author: magnu
"""
import numpy as np
import json
import pygame, sys
import os

class NodeSystem:
    def __init__(self, screen, n):
        self.screen = screen
        self.nodes = np.zeros((n, 5))
        self.nodes[:, [0, 1]] = np.random.randint([self.screen.get_width(), self.screen.get_height()], size = (n, 2))
        self.nodes[:, [3, 4]] = np.random.rand(n, 2)*2-1
        self.sick_color = 255, 0, 0
        self.healthy_color = 0, 255, 0
        self.node_radius = 8


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



    def drawNodes(self):

        for row in self.nodes:
            pygame.draw.circle(self.screen, self.color(row), row[[0,1]], self.node_radius, 0)


    def updatePosition(self):
        self.nodes[:, [0,1]] += self.nodes[:, [3,4]]


    def writeToJson(self):
        with open(r"C:\Users\magnu\Desktop\School\4. Semester\Semesterprojekt\Kode\log.json", "w"):
            lists = dict(self.nodes.tolist())
            data = {lists}
            json_strings = json.dumps(data)
            print(json_strings)


            #path = os.path.dirname(path)
            #fileName = "jsonDump"
            #data = {self.nodes}