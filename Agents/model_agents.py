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

start = time.process_time()

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2)+((agents_row_a._y - agents_row_b._y)**2))**0.5

seed = 1
random.seed(seed)

num_of_agents = 2
num_of_iterations = 3
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    print("Agents before move", j, agents)
    for i in range(num_of_agents):
        agents[i].move()
        print("Agent", i, "after move", agents[i])
    print("Agents after move", j, agents)

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)
        
end = time.process_time()

print("time = " + str(end - start))

print(agents)

#print(a.y, a.x)
#a.move()
#print(a.y, a.x)