import main


n = 200 #pop density
iterations = 1000 #number of iterations
masks = 20 # percentage of mask-wearers
vax = 10 #percentage of vaccinated nodes
logsteps = 10 # log every nth frame

main.runSim(n, iterations, masks, vax, logsteps)
