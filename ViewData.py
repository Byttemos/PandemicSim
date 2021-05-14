import numpy as np
import matplotlib.pyplot as plt
import main
import nodeSystem as ns
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, data, pop_size):
        self.fig, self.ax = plt.subplots()
        self.data = data
        self.pop_size=pop_size
        self.ani = animation.FuncAnimation(self.fig, self.update, interval = 5,
                                           init_func=self.setup_plot, repeat = False, frames = self.data.shape[0], blit=True)

    def setup_plot(self):
        x, y = self.data[0, :, 0], self.data[0, :, 1]
        self.scat = self.ax.scatter(x, y, cmap="jet", edgecolor="k")
        return self.scat,


    def update(self, i):
        """Update the scatter plot."""
        data = self.data[i, :, :]
        # Set x and y data...
        self.scat.set_offsets(data[:, :2])
        # Set sizes...
        # self.scat.set_sizes(300 * abs(data[:, 2])**1.5 + 100)
        sizes = np.ones(data.shape[0])
        self.scat.set_sizes(sizes + 2)
        # # Set colors..
        self.scat.set_array(data[:, 2])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

def init_animation():
    fig, ax = plt.subplots()
    scat = ax.scatter(data[(i-1)*pop:i*pop, 0], data[(i-1)*pop:i*pop, 1])
    plt.title("Simulation visualization")


def animate_plot(i, pop):
    pass
    # ax.scatter(data[(i-1)*pop:i*pop, 0], data[(i-1)*pop:i*pop, 1])

def plot_nodes(pop, iterations):
    # animation = FuncAnimation(fig, animate_plot,fargs=(pop,), frames=iterations, interval=20)

    # data=np.genfromtxt("simlog.csv", delimiter=",")
    with open("simlog.npy", "rb") as f:
        data = np.load(f)

    # a = data[:pop, :].copy()
    # data = data.reshape((pop, 5, (data.shape[0]//pop)))
    # print(a)
    # print(data[:,:,0])
    ac = AnimatedScatter(data, pop)
    # data = np.genfromtxt("simlog.csv", delimiter=",")
    # for i in range(1,iterations):
        # plt.scatter(data[(i-1)*pop:i*pop, 0], data[(i-1)*pop:i*pop, 1])

    plt.show()
