# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:36:33 2021

@author: Sam
"""


#import random
#import operator
import matplotlib.pyplot
import agentframework
import time
import random
from random import shuffle
import csv

start = time.process_time()

environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
            
#print(environment)
#def distance_between(agents_row_a, agents_row_b):
   #return (((agents_row_a._x - agents_row_b._x)**2)+((agents_row_a._y - agents_row_b._y)**2))**0.5

seed = 1
random.seed(seed)

num_of_agents = 2
num_of_iterations = 50
neighbourhood = 20
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

# Move the agents.
for j in range(num_of_iterations):
    print("Agents before move", j, agents)
    for i in range(num_of_agents):
        shuffle(agents)
        agents[i].move()
        agents[i].eat()
        #agents[i].eatall()
        agents[i].drop()
        agents[i].share_with_neighbours(neighbourhood)
        print("Agent", i, "after move:", agents[i])
    print("Agents after move", j, agents)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()

#for agents_row_a in agents:
   #for agents_row_b in agents:
        #distance = distance_between(agents_row_a, agents_row_b)
        #print(distance)
        
end = time.process_time()

print("time = " + str(end - start))
#print(environment)
#print(agents)
#print(shuffle)
#print(a.y, a.x)
#a.move()
#print(a.y, a.x)