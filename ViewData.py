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
        
        """
        if np.any(self.data[:, 4] == 1):
            self.scat.set_color("red")
        """
        
        return self.scat,
        #self.ax.text(1, 1, "Deathcount: " + sum(self.data[:,:,8]))

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
    plt.plot(gwaf[:,4], color="red")
    plt.plot(gwaf[:, 8], color="black")
    plt.plot(gwaf[:, 6], color="magenta")
    plt.xlabel("Days")
    plt.legend(["Infected", "Dead", "Immune"], loc="lower right")
    plt.ylim([0,100])
    # print(gwaf)
    # plt.plot(gwaf, iterations)
    plt.show()

 
class Cursor:
    """
    A cross hair cursor.
    """
    def __init__(self, ax):
        self.ax = ax
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        # text location in axes coordinates
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw

    def on_mouse_move(self, event):
        if not event.inaxes:
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.draw()
        else:
            self.set_cross_hair_visible(True)
            x, y = event.xdata, event.ydata
            # update the line positions
            self.horizontal_line.set_ydata(y)
            self.vertical_line.set_xdata(x)
            self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))
            self.ax.figure.canvas.draw()


x = np.arange(0, 1, 0.01)
y = np.sin(2 * 2 * np.pi * x)

fig, ax = plt.subplots()
ax.set_title('Simple cursor')
ax.plot(x, y, 'o')
cursor = Cursor(ax)
fig.canvas.mpl_connect('motion_notify_event', cursor.on_mouse_move)
