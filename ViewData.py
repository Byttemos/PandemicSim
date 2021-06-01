from tkinter import Label
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

        #self.scat = self.ax.scatter(x, y, edgecolors="none", color="red")
        return self.scat,


    def update(self, i):
        """Update the scatter plot."""
        data = self.data[i, :, :]
        # Set x and y data...
        self.scat.set_offsets(data[:, :2])
        sizes = np.ones(data.shape[0])
        self.scat.set_sizes(sizes + 30)
        self.scat.set_array(data[:, 2])
        x = self.data[:0]
        y = self.data[:1]
        colors = self.data[:2]
        plt.scatter(x, y, c=colors, cmap='Accent')
        plt.savefig(sys.stdout.buffer)
        sys.stdout.flush()
        return self.scat,
        #self.ax.text(1, 1, "Deathcount: " + sum(self.data[:,:,8]))

def plot_nodes(pop, iterations):
    with open("simlog.npy", "rb") as f:
        data = np.load(f)
    ac = AnimatedScatter(data, pop)
    plt.show()


def show_graph(iterations):
    plt.cla()
    with open("simlog.npy", "rb") as f:
        data = np.load(f)
    # print(data[:, :, 4].sum())
    gwaf = data.sum(axis = 1)
    plt.plot(gwaf[:,4], color="red")
    plt.plot(gwaf[:, 8], color="black")
    plt.plot(gwaf[:, 6], color="magenta")
    plt.plot(int(data.shape[1])-(gwaf[:,4]+gwaf[:,8]+gwaf[:,6]))
    plt.xlabel("Days")
    plt.legend(["Infected", "Dead", "Immune", "susceptible"], loc="lower right")
    plt.ylim([0,100])
    plt.show()
