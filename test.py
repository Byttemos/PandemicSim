
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
import sys, pygame
from random import randint
# test 

# Set size of pygame window
resolution = width, height = 800, 600
screen = pygame.display.set_mode(resolution)

class Node:
    """ Constructor. instantiate n nodes with speed, position and contagion status """
    def __init__(self, status):
        self.speed = 1
        self.pos = [randint(width), randint(height)]
        self.status = status


def healthy(args):
    pass

popDensity = 6969
for i in range(popDensity):
    human = Node(healthy)


def sick(args):
    pass

