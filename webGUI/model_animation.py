# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:36:33 2021

@author: Sam
"""


## import all packages
import tkinter
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
plt.ioff()
import agentframework
import time
import random
from random import shuffle
import csv
import matplotlib.animation

import requests
import bs4

##initiate process time monitoring
start = time.process_time()

##Get data from web to use within model
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs) 

##import environment data into model
environment = []
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

## set random seed
##seed = 1
##random.seed(seed)

num_of_agents = 2
num_of_iterations = 100
neighbourhood = 1
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment,agents, y, x))
        
carry_on = True

def update(frame_number):
    
    fig.clear()
    global carry_on

    # Move the agents
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            print("Agent", i, "before move", agents[i])
        for i in range(num_of_agents):
            #shuffle(agents)
            agents[i].move()
            agents[i].eat()
            #agents[i].eatall()
            agents[i].drop()
            agents[i].share_with_neighbours(neighbourhood)
            print("Agent", i, "after move", agents[i])
            #print("Agents after move", agents)
            
    if agents[i].record > 4:
        carry_on = False
        print("stopping condition")

        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
        print("Agent ", i, "x = ", agents[i]._x, "y = ", agents[i]._y, "Store = ", agents[i].store, "sick count = ", agents[i].record)
        matplotlib.pyplot.xlim(0, 100)
        matplotlib.pyplot.ylim(0, 100)
        matplotlib.pyplot.imshow(environment)
 
##stopping condition not working
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False, interval=1)
    canvas.draw()
    
end = time.process_time()

print("time = " + str(end - start))
    
window = tkinter.Tk()
window.title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=window)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()