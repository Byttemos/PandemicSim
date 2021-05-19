import numpy as np
import matplotlib.pyplot as plt
import main
# from nodeSystem import NodeSystem as ns
import matplotlib.animation as animation


class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, data, pop_size):
        self.fig, self.ax = plt.subplots()
        self.data = data
        self.pop_size=pop_size
        self.ani = animation.FuncAnimation(self.fig, self.update, interval = 5,
                                           init_func=self.setup_plot, repeat = False, frames = self.data.shape[0], blit=True)
        self.colors = ["red", "green", "black", "blue", "purple", "pink"]

    def setup_plot(self):
        x, y = self.data[0, :, 0], self.data[0, :, 1]
        # self.scat = self.ax.scatter(x, y, cmap="jet", edgecolor="k", c="red")

        self.scat = self.ax.scatter(x, y, edgecolors="none", color="red")

        return self.scat,


    def update(self, i):
        """Update the scatter plot."""
        data = self.data[i, :, :]
        # Set x and y data...
        self.scat.set_offsets(data[:, :2])

        sizes = np.ones(data.shape[0])
        self.scat.set_sizes(sizes + 30)
        self.scat.set_array(data[:, 2])
        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,
        self.ax.text(1, 1, "Deathcount: " + sum(self.data[:,:,8]))

def plot_nodes(pop, iterations):

    with open("simlog.npy", "rb") as f:
        data = np.load(f)


    ac = AnimatedScatter(data, pop)
    plt.show()

def show_graph(iterations):
    with open("simlog.npy", "rb") as f:
        data = np.load(f)
    # print(data[:, :, 4].sum())
    gwaf = data.sum(axis = 1)
    plt.plot(gwaf[:,4])
    plt.plot(gwaf[:, 8])
    plt.plot(gwaf[:, 6])
    plt.xlabel("Days")
    # print(gwaf)
    # plt.plot(gwaf, iterations)
    plt.show()
