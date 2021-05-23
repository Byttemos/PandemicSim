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
from nodeSystem import NodeSystem as ns
import numpy as np

def callbacktest(nodesystem):
    print(nodesystem.nodes[:, 4].sum())

def runSim(n, iteration_number, mask_procent, mortality_rate, log_steps = 10, callback = None):

    nodesys = ns(n, mask_procent, mortality_rate)

    data = np.zeros((1, 12))
    for i in range(iteration_number):
        nodesys.updatePosition()
        nodesys.collision_detection()

        if (data == 0).all():
            data = nodesys.nodes

        else:
            data = nodesys.logData(data) if i % log_steps == 0 else data

        if callback:
            callback(nodesys)



    with open("simlog.npy", "wb") as f:
        np.save(f, data)
