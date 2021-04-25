from tkinter import *
import main



def run():
    main.runSim(population_slider.get(), iteration_slider.get())
#Instantiate root window
root = Tk()

welcomemsg = Label(root, text="Greetings from the PandemicSim dev team! \n Select population size")
welcomemsg.grid(row=0, column=0)

population_slider = Scale(root, from_=1, to=100000, orient=HORIZONTAL, label="Population:")
population_slider.grid(row=1, column=0)

iteration_slider = Scale(root, from_=1, to=10000, orient=HORIZONTAL, label="Iterations:")
iteration_slider.grid(row=2, column=0)

runsim_button = Button(root, text="Run Simulation", bg="#82ff63", command=run)
runsim_button.grid(row=3, column=0)

#Run loop of root window
root.mainloop()
