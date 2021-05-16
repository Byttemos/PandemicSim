import numpy as np
import matplotlib.pyplot as plt
import main
#import nodeSystem as ns
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

        sizes = np.ones(data.shape[0])
        self.scat.set_sizes(sizes + 2)
        self.scat.set_array(data[:, 2])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,

def plot_nodes(pop, iterations):

    with open("simlog.npy", "rb") as f:
        data = np.load(f)

    ac = AnimatedScatter(data, pop)

    plt.show()
