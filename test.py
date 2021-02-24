
"""

Pandemic Contagion Simulator V.0.2
Copyright (C) 2021  Bjørn Utzon, Henrik Riskær, Magnus Nielsen, Nicolai Nielsen, Lau Sivertsen

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
import pygame, sys, time
from Node import Node

import numpy as np
from dataclasses import dataclass
# test 
pygame.init()
# Set size of pygame window
resolution = width, height = 800, 600
screen = pygame.display.set_mode(resolution)
print(screen.get_width())
popDensity = 10



black = 0, 0, 0

nodelist = []



for i in range(popDensity):
    nodelist.append(Node(screen))


nodelist[0].makeSick()

drawing = True
pygame.display.set_caption("PandemicSim")
counter = 0
print(type(nodelist[0].pos))
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    # nodelist[0] == node
    screen.fill(black)
    for node in nodelist:
        node.draw()
        node.update()
        for somenode in nodelist:
            if node == somenode:
                continue
            else:
                node.spreadInfection(somenode)
    pygame.display.flip()
