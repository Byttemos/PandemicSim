from tkinter import *
import main, ViewData
import sys


def run():
    runsim_button.configure(text="Running Simulation...")
    main.runSim(population_slider.get(), iteration_slider.get(), masks_slider.get(), vaccer_slider.get(), mortality_rate_as_float)
    runsim_button.configure(text="Complete Simulation")
    view_results_button.grid(row=8, column=0)


def view_results():

    ViewData.show_graph(iteration_slider.get())
#Instantiate root window
root = Tk()

welcomemsg = Label(root, text="Greetings from the PandemicSim dev team! \n Select a population size")
welcomemsg.grid(row=0, column=0)

population_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Population:", length=220, resolution=10)
population_slider.grid(row=1, column=0)

masks_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Number of people with masks ( IN %):", length=220, resolution=5)
masks_slider.grid(row=2, column=0)

vaccer_slider =Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Number of people vaccinated ( IN %):", length=220, resolution=5)
vaccer_slider.grid(row=3, column=0)

mortality_msg = Label(root, text="Insert mortality rate")
mortality_msg.grid(row=4, column=0, sticky=W, padx=10)
mortality_textfield = Entry(root,)
mortality_textfield.grid(row=5, column=0, padx=10, sticky=W)
mortality_textfield.insert(0, "2.07")
mortality_rate_as_float = float(mortality_textfield.get())

iteration_slider = Scale(root, from_=0, to=10000, orient=HORIZONTAL, label="Iterations:", length=220, resolution=10)
iteration_slider.grid(row=6, column=0)

runsim_button = Button(root, text="Run Simulation", bg="#82ff63", command=run)
runsim_button.grid(row=7, column=0)

view_results_button = Button(root, text="View Results", bg="#0096FF", command=view_results)

exit_button = Button(root, text="Exit application", bg="#FF0000",command= lambda: sys.exit())
exit_button.grid(row=9, column=0)

#Run loop of root window
root.mainloop()
