import numpy as np
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
        dm = distance_matrix(self.nodes[:, :2], self.nodes[:, :2])
        collision_pairs = np.tril(list(zip(*np.where((dm < self.node_radius*2) & (dm != 0.0)))))
        self.interact(collision_pairs)

    def logData(self, data):
        """Write data to .npy file"""
        if len(data.shape) == 2:
            return np.stack((data, self.nodes))
        else:
            return np.concatenate((data, self.nodes[None, :, :]))


    def interact(self, collided_nodes):
        """Determine outcome of a collision between two nodes based on the nodes' propertie"""
        for i in collided_nodes:
            if not self.nodes[collided_nodes[i][0], 4]:
                print("THIS NODE IS HELFY")
            else:
                print("DIS NOTE GUNNA DIE")


    def infect(node):
        """Spread infection from one node to a collided node. receives sliced array of nodes to be infected"""
        pass



    def updatePosition(self):
        """Increment all node positions and reverse velocity if node is out of bounds"""
        self.nodes[:, [0,1]] += self.nodes[:, [2,3]]
        self.nodes[self.nodes[:, 0] < 0, 2] *= (-1)
        self.nodes[self.nodes[:, 0] > 1500, 2] *= (-1)
        self.nodes[self.nodes[:, 1] < 0, 3] *= (-1)
        self.nodes[self.nodes[:, 1] > 1000, 3] *= (-1)
