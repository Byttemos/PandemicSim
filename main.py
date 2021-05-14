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
import pygame, sys, time, os
from nodeSystem import NodeSystem as ns
import numpy as np
from dataclasses import dataclass

def callbacktest(nodesystem):
    print(nodesystem.nodes)

def runSim(n, iteration_number, log_steps = 10, callback = callbacktest):

    nodesys = ns(n)
    data = np.zeros((1,5))

    for i in range(iteration_number):
        nodesys.updatePosition()
        data = nodesys.logData(data) if i % log_steps == 0 else data

        if callback:
            callback(nodesys)

    np.savetxt("simlog.csv", data, delimiter=",")


