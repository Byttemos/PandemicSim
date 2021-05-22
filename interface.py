import tkinter as tk
import sys


# def run():
#     runsim_button.configure(text="Running Simulation...")
#     main.runSim(population_slider.get(), iteration_slider.get(), masks_slider.get(), vaccer_slider.get(), mortality_rate_as_float)
#     runsim_button.configure(text="Complete Simulation")
#     view_results_graph_button.grid(row=8, column=0)
#     view_results_scatter_button.grid(row=9, column=0)


# def view_results_graph():

#     ViewData.show_graph(iteration_slider.get())

# def view_results_scatter():

#     ViewData.plot_nodes(population_slider.get(), iteration_slider.get())
    
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

vaccer_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Number of people vaccinated ( IN %):", length=220, resolution=5)
vaccer_slider.grid(row=3, column=0)
vaccer_slider.set(20)

mortality_msg = tk.Label(root, text="Insert mortality rate")
mortality_msg.grid(row=4, column=0)
mortality_textfield = tk.Entry(root,)
mortality_textfield.grid(row=5, column=0)
mortality_textfield.insert(0, "2.7")
mortality_rate_as_float = float(mortality_textfield.get())

iteration_slider = tk.Scale(root, from_=0, to=10000, orient=tk.HORIZONTAL, label="Iterations:", length=220, resolution=10)
iteration_slider.grid(row=6, column=0)
iteration_slider.set(4000)

runsim_button = tk.Button(root, text="Run Simulation", bg="#82ff63", command=run)
runsim_button.grid(row=7, column=0)



view_results_graph_button = tk.Button(root, text="View Results", bg="#0096FF", command=view_results_graph)

view_results_scatter_button = tk.Button(root, text="View Scatter Plot", bg="#0096FF", command=view_results_scatter)

exit_button = tk.Button(root, text="Exit Application", bg="#FF0000",command= lambda: sys.exit())
exit_button.grid(row=10, column=0)



"""Helper functions to parse arguments to parameters.py"""
def get_population():
    return population_slider.get()

def get_vaccinated():
    return vaccer_slider.get()

def get_masks():
    return masks_slider.get()

def get_iterations():
    return iteration_slider.get()

def get_mortality_rate():
    return float(mortality_textfield.get())

#Run loop of root window
root.mainloop()
