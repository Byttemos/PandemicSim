import main, ViewData
import tkinter as tk
import sys


def run():
    runsim_button.configure(text="Running Simulation...")
    main.runSim(population_slider.get(), iteration_slider.get(), masks_slider.get(), mortality_slider.get())
    runsim_button.configure(text="Done!")
    view_results_graph_button.grid(row=7, column=0)
    view_results_scatter_button.grid(row=8, column=0)


def view_results_graph():

    runsim_button.configure(text="Run Simulation")
    ViewData.show_graph(iteration_slider.get())

def view_results_scatter():

    runsim_button.configure(text="Run Simulation")
    ViewData.plot_nodes(population_slider.get(), iteration_slider.get())
    
#Instantiate root window
root = tk.Tk()

welcomemsg = tk.Label(root, text="Greetings from the PandemicSim dev team! \n Select a population size")
welcomemsg.grid(row=0, column=0)

population_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Population:", length=220, resolution=10)
population_slider.grid(row=1, column=0)
population_slider.set(100)

masks_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Number of people with masks ( IN %):", length=220, resolution=5)
masks_slider.grid(row=2, column=0)
masks_slider.set(20)

mortality_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Mortality rate:", length=150, resolution=0.1)
mortality_slider.grid(row=4, column=0)
mortality_slider.set(2)

iteration_slider = tk.Scale(root, from_=0, to=10000, orient=tk.HORIZONTAL, label="Iterations:", length=220, resolution=10)
iteration_slider.grid(row=5, column=0)
iteration_slider.set(4000)

runsim_button = tk.Button(root, text="Run Simulation", bg="#82ff63", command=run)
runsim_button.grid(row=6, column=0)



view_results_graph_button = tk.Button(root, text="View Results", bg="#0096FF", command=view_results_graph)

view_results_scatter_button = tk.Button(root, text="View Scatter Plot", bg="#0096FF", command=view_results_scatter)

exit_button = tk.Button(root, text="Exit Application", bg="#FF0000",command= lambda: sys.exit())
exit_button.grid(row=9, column=0)



#Run loop of root window
root.mainloop()
