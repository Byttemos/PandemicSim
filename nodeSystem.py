import numpy as np
from scipy.spatial import distance_matrix
# import interface
class NodeSystem:
    def __init__(self, n, mask_procent, vac_procent, mortality_rate):
        """0: xpos, 1:ypos, 2: Vx, 3: Vy, 4: sick, 5:mask, 6: immune, 7: vaxxed, 8: ded, 9: sick counter, 10: are you gonna fucking die?"""
        self.nodes = np.zeros((n, 11))
        self.nodes[:, [0, 1]] = np.random.randint([500, 500], size = (n, 2))
        self.nodes[:, [2, 3]] = np.random.randn(n, 2)
        self.nodes[:, 10] = np.random.randint(100, size = n)
        self.healthy_color_mask = 0, 103, 0
        self.healthy_color_no_mask = 0, 255, 0
        self.sick_color_mask = 255, 100, 240
        self.sick_color_no_mask = 150, 0 ,0
        self.vaccinated = 0, 0, 255
        self.immune = 127, 0, 255
        self.dead = 0, 0, 0
        self.node_radius = 2
        self.mortality_rate = mortality_rate
        self.nodes[-1, 4] = 1 #create patient zero
        masks = (int(n/100))*int(mask_procent)
        self.nodes[[range(masks)], 5] = 1 #give people masks
        self.infection_risk = 0.9

    def switch_state(self, row):
        """4 = Healthy bool, 5 = Mask bool, 6 = Immune, 7 = Vaccinated, 8 = Dead"""
        states = np.array([4,5,6,7,8])
        find_states = np.where(nodes== 1)

        if find_states([8]): #if dead
            dead_x_velocity = self.nodes[: ,2]= 0
            dead_y_velocity = self.nodes[:, 3] = 0
            return self.dead

        if find_states([7]): #if vaccinated
            #Do something but don't interact if collision
            return self.vaccinated

        if find_states([6]): #if immune
            #Pause collision contagion for given amount of time
            self.immune 
            time.sleep(5)
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
        dm = np.tril(distance_matrix(self.nodes[:, :2], self.nodes[:, :2]))
        collision_pairs = list(zip(*np.where((dm < self.node_radius*2) & (dm != 0.0))))
        self.interact(collision_pairs)

    def logData(self, data):
        """Write data to .npy file"""
        if len(data.shape) == 2:
            return np.stack((data, self.nodes))
        else:
            return np.concatenate((data, self.nodes[None, :, :]))


    def interact(self, collided_nodes):
        """Determine outcome of a collision between two nodes based on the nodes' propertie"""
        for first, second in collided_nodes:
            
            if self.nodes[[first], 6:9].sum() >= 1 or self.nodes[[second], 6:9].sum() >= 1:
                #check if any node is dead
                pass
            elif  self.nodes[[first], 4] == 1 and self.nodes[[second], 4] == 1:
                #check if both nodes are sick as fuck bruh
                pass
            elif  self.nodes[[first], 4] == 0 and self.nodes[[second], 4] == 0:
                #check if both nodes are healthy
                pass
            else:
                infection = np.random.rand()
                instance_risk = self.infection_risk + self.nodes[[second], 5]/100 + self.nodes[[first], 5]/100
                instance_risk = instance_risk[0]
                if not infection > instance_risk:
                    if self.nodes[first, 4] == 0:
                        self.nodes[first, 4] = 1
                    else:
                        self.nodes[second, 4] = 1



    def updatePosition(self):
        """Increment all node positions and reverse velocity if node is out of bounds"""
        self.nodes[:, [0,1]] += self.nodes[:, [2,3]]
        self.nodes[self.nodes[:, 0] < 0, 2] *= (-1)
        self.nodes[self.nodes[:, 0] > 500, 2] *= (-1)
        self.nodes[self.nodes[:, 1] < 0, 3] *= (-1)
        self.nodes[self.nodes[:, 1] > 500, 3] *= (-1)
        """increment sick counter until 140 (14 days) and determine whether the node dies or becomes immune"""
        self.nodes[self.nodes[:, 4] == 1, 9] += 1
        # death_nodes = self.nodes[self.nodes[:, 10] <= 50]
        mask = np.where((self.nodes[:, 10] <= self.mortality_rate) & (self.nodes[:, 9] == 400), True, False)
        self.nodes[mask, 8] = 1
        self.nodes[mask, 4] = 0
        # survivor_nodes = self.nodes[self.nodes[:, 10] > self.mortality_rate]
        survivor_nodes = np.where((self.nodes[:, 10] > self.mortality_rate) & (self.nodes[:,9] == 400), True, False)
        self.nodes[survivor_nodes, 4] = 0
        self.nodes[survivor_nodes, 6] = 1

