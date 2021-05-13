from tkinter import *
import main

runString = "Run simulation"


def run():
    main.runSim(population_slider.get(), iteration_slider.get())
    runString = "Simulation done!"
#Instantiate root window
root = Tk()

welcomemsg = Label(root, text="Greetings from the PandemicSim dev team! \n Select population size")
welcomemsg.grid(row=0, column=0)

population_slider = Scale(root, from_=1, to=50000, orient=HORIZONTAL, label="Population:", length=210, resolution=200)
population_slider.grid(row=1, column=0)

masks_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Number of people with masks ( IN %):", length=220, resolution=5)
masks_slider.grid(row=2, column=0)

vaccerSlider =Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Number of people vaccinated ( IN %):", length=220, resolution=5)
vaccerSlider.grid(row=3, column=0)

testSlider =Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Number of test:", length=220, resolution=5)
testSlider.grid(row=4, column=0)

iteration_slider = Scale(root, from_=1, to=10000, orient=HORIZONTAL, label="Iterations:", length=210, resolution=10)
iteration_slider.grid(row=5, column=0)

runsim_button = Button(root, text=runString, bg="#82ff63", command=run)
runsim_button.grid(row=6, column=0)

#Run loop of root window
root.mainloop()
