# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:36:33 2021

@author: Sam
"""


import matplotlib.pyplot
import agentframework
import time
import random
from random import shuffle
import csv
import matplotlib.animation 

start = time.process_time()

environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

seed = 1
random.seed(seed)

num_of_agents = 10
num_of_iterations = 40
neighbourhood = 1
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
    
carry_on = True

def update(frame_number):
    
    fig.clear()
    global carry_on

    # Move the agents
    for j in range(num_of_iterations):
        print("Agents before move", j, agents)
        for i in range(num_of_agents):
            #shuffle(agents)
            agents[i].move()
            agents[i].eat()
            #agents[i].eatall()
            agents[i].drop()
            agents[i].share_with_neighbours(neighbourhood)
            print("Agent", i, "after move:", agents[i])
        print("Agents after move", j, agents)
        
    if agents[i].record >= 20:
        carry_on = False
        print("stopping condition")
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
        print(agents[i]._x,agents[i]._y)
    #matplotlib.pyplot.show()
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)
    
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False, interval = 1)


matplotlib.pyplot.show()
        
end = time.process_time()

print("time = " + str(end - start))