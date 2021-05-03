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
#print(td_ys)
#print(td_xs) 

## Create empty agents (sheep) list
agents = []

## Create empty list for wolves
wolves = []

## Create empty environment list
environment = []

## Define variables
## Define how many sheep in model
num_of_agents = 200
## Define how many wolves in model
num_of_wolves = 2
## Define how many iterations
num_of_iterations = 10
## Define distance at which agents interact with each other
neighbourhood = 5

## Import environment data into model
with open('in.txt', newline='') as f:
    ## load in textfile with environment data
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
f.close()  

## calculate total sum of values in environment data
total = sum(sum(x) for x in environment) 
print(total)

## set random seed
##seed = 1
##random.seed(seed)

## set dimension of figure
fig = matplotlib.pyplot.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents (sheep)
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
#print(agents)

# Make the wolves
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment, neighbourhood))
    

# Set frames for animation, define graph dimensions and add environment data
def update(frame_number):
    global carry_on
    fig.clear()
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)

    # Move the agents
    for j in range(num_of_iterations):
        random.shuffle(agents)
        #for i in range(num_of_agents):
            #print("Agent", i, "before move", agents[i])
        for agent in agents:
            agent.move()
            agent.eat()
            agent.share_with_neighbours(neighbourhood, agents)
            #print("Agent", i, "after move", agents[i])
            #print("Agents after move", agents)
        print (sum(sum(x) for x in environment))
            
    # Move the wolves
    for wolf in wolves:
        wolf.move()
        wolf.eat_agents(neighbourhood, wolves, agents)
    
    # Add agents data to graph and style
    for agent in agents:
        matplotlib.pyplot.scatter(agent.x, agent.y, color='white', marker="D", s=40)
        matplotlib.pyplot.annotate(agent.record, (agent.x,agent.y), fontsize=20, color="red", weight="bold")
        print("x = ", agent.x, "y = ", agent.y, "Store = ", agent.store, "sick count = ", agent.record)
     
    # Add wolves data to graph and style 
    for wolf in wolves:
        matplotlib.pyplot.scatter(wolf.x, wolf.y, marker="D", color='black',s=60)
        matplotlib.pyplot.annotate(wolf.count, (wolf.x,wolf.y), fontsize=20, color="white", weight="bold")
    
    # Stopping Conditions
    # Sum all values in environment, when less than 90% of environment, stop simulation 
    if sum(sum(x) for x in environment) < total*0.90:
        carry_on = False
        print("Stopping condition met - Environment depleted by %10")  #"simulaiton time = " + str(end - start))
    
    # Return number of items in agent list and stop simulation when all sheep have been eaten
    if len(agents) == 0:
        carry_on = False
        print("Stopping condition met - All sheep have been eaten!") #"simualtion time = " + str(end - start))
    
    ## Write out environment results to text file
    with open('out.txt', 'w', newline='') as f:     
        env_writer = csv.writer(f)     
        for row in environment:         
            env_writer.writerow(row)
 
carry_on = True

## 
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
## Inititate simulation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function)
    canvas.draw()
    
#print("time = " + str(end - start))
 
## GUI settings / design   
window = tkinter.Tk()
window.title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=window)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

window.mainloop()

#end = time.process_time()