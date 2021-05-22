import main


n = 20000 #pop density
iterations = 1 #number of iterations
masks = 20 # percentage of mask-wearers
vax = 10 #percentage of vaccinated nodes
logsteps = 1 # log every nth frame

main.runSim(n, iterations, masks, vax, logsteps)
