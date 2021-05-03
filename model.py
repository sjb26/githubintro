# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:36:33 2021

@author: Sam
"""
import random
import operator
import matplotlib.pyplot

# Set up variables #create random value with 100m by 100m grid

agents = []
agents.append([random.randint(0,99),random.randint(0,99)])

# Random walk one step
if random.randint(0,99) < 0.5:
    agents[0][0]= agents[0][0] + 1
else:
     agents[0][0]= agents[0][0] - 1   
     
if random.randint(0,99) < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1
     
agents.append([random.randint(0,99),random.randint(0,99)])

#Random walk one step
if random.randint(0,99) < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
     agents[1][0] = agents[1][0] - 1   
     
if random.randint(0,99) < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1
    
y_diff = (agents[0][0] - agents[1][0])
y_diffsq = y_diff * y_diff
x_diff = (agents[0][1]- agents[1][1])
x_diffsq = x_diff * x_diff

sum = y_diffsq + x_diffsq
answer = sum**0.5

#create the furthest east coordinate and seperate from list into values
east_yx = max(agents, key=operator.itemgetter(1))
y_indices = [0]
east_y = [east_yx[index] for index in y_indices]
x_indices = [1]
east_x = [east_yx[index] for index in x_indices]
    
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(east_x, east_y, color='red')
matplotlib.pyplot.show()

print(answer)
print(agents)
print(max(agents, key=operator.itemgetter(1)))
print(east_yx)
print(east_y)