
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
import pygame, sys
import numpy as np
# test 
pygame.init()
# Set size of pygame window
resolution = width, height = 800, 600
screen = pygame.display.set_mode(resolution)


class Node:
    """ Constructor. instantiate n nodes with speed, position and contagion status """
    def __init__(self, status, quarantined, ):
        self.speed = 1
        self.pos = [np.random.randint(width), np.random.randint(height)]
        self.status = status
        self.quarantined = quarantined
        self.color = np.random.randint(255, size=3)

def healthy(args):
    pass
black = 255, 255, 255
nodelist = []
popDensity = 1000
for i in range(popDensity):
    nodelist.append(Node(healthy, False))


def sick(args):
    pass


drawing = True
pygame.display.set_caption("PandemicSim")
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # nodelist[0] == node
    screen.fill(black)
    for node in nodelist:
        pygame.draw.circle(screen, node.color, node.pos, 8, 0)
    pygame.display.flip()