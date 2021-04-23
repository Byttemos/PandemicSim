from tkinter import *
import main



def run():
    main.runSim(population_slider.get(), iteration_slider.get())
#Instantiate root window
root = Tk()

welcomemsg = Label(root, text="Greetings from the PandemicSim dev team! Select population size")
welcomemsg.grid(row=0, column=0)

pop = Label(root, text="population:")
pop.grid(row=1, column=0)

population_slider = Scale(root, from_=1, to=100000, orient=HORIZONTAL)
population_slider.grid(row=2, column=0)

iter = Label(root, text="Iterations:")
iter.grid(row=3, column=0)

iteration_slider = Scale(root, from_=1, to=10000, orient=HORIZONTAL)
iteration_slider.grid(row=4, column=0)

runsim_button = Button(root, text="Run Simulation", bg="#82ff63", command=run)
runsim_button.grid(row=5, column=0)

#Run loop of root window
root.mainloop()