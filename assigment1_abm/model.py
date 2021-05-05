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

##Get data from web to use within model
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)  #test that webdata is being read/imported
#print(td_xs) #test that webdata is being read/importe 

## Create empty agents (sheep) list
agents = []

## Create empty list for wolves
wolves = []

## Create empty environment list
environment = []

## Define variables
## Define how many sheep in model
num_of_agents = 100
## Define how many wolves in model
num_of_wolves = 0
## Define how many iterations - feeds into how many often frames are shown in the GUI
num_of_iterations = 1
## Define distance at which agents interact with each other
neighbourhood = 5
## Define the % the environment should be depleted by to enable stopping condition
percentenvironmentdepleted = 50 #value must be between 0 and 100

edepleted = (100-percentenvironmentdepleted)/100 #feeds into stopping condition calculation

## Import environment data into model
# open textfile with environment data in
with open('in.txt', newline='') as f:
    ## load in textfile with environment data
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []		 #create empty list for rowlist
        for value in row:   
            rowlist.append(value)  #add value to rowlist
        environment.append(rowlist)  #append the rowlists to the environment variable
f.close() #close textfile  

## calculate total sum of values in environment data
total = sum(sum(x) for x in environment) 
print(total)

## set random seed # The random seed was originally used to ensure the model was running properly with the same set of values when initial changes were made to the model. This has now been replaced with the data retrieved from the web.
##seed = 1
##random.seed(seed)

## set dimension of figure
fig = matplotlib.pyplot.figure(figsize=(10, 10))
ax = fig.add_axes([0, 0, 1, 1])

##initiate process time monitoring
start = time.process_time()

# Make the agents (sheep) and append to agentframework and environment
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
#print(agents)

# Make the wolves and append to agentframework and environment
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(environment, neighbourhood))


# Set frames for animation, define graph dimensions and display the environment
def update(frame_number):
    global carry_on
    fig.clear()
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment)

    # Move the agents, make them eat and share with neighbours for the defined number of iterations
    for j in range(num_of_iterations):
        random.shuffle(agents)
        #for i in range(num_of_agents):  
            #print("Agent", i, "before move", agents[i])
        for agent in agents:
            agent.move()
            agent.eat()
            agent.share_with_neighbours(neighbourhood, agents)
            #print("Agent", i, "after move", agents[i]) #removed as altered 'for i in range' to 'for agent in agents'.
            #print("Agents after move", agents) 
        print (sum(sum(x) for x in environment)) #print the environment sum after every iteration, tracks how much is being eaten in console
            
    # Move the wolves and make them eat sheep
    for wolf in wolves:
        wolf.move()
        wolf.eat_agents(neighbourhood, wolves, agents)
    
    # Add agents data to graph and style
    for agent in agents:
        matplotlib.pyplot.scatter(agent.x, agent.y, color='white', marker="D", s=40)  #add agent data to animation and style as white diamond
        matplotlib.pyplot.annotate(agent.record, (agent.x,agent.y), fontsize=20, color="red", weight="bold") #annotate each agent with how many times they have been sick
        print("x = ", agent.x, "y = ", agent.y, "Store = ", agent.store, "sick count = ", agent.record) # for every agent report x and y, how much is in store and number of times sick in console
     
    # Add wolves data to graph and style 
    for wolf in wolves:
        matplotlib.pyplot.scatter(wolf.x, wolf.y, marker="D", color='black',s=60) #add wolf to animation and style as black diamond
        matplotlib.pyplot.annotate(wolf.count, (wolf.x,wolf.y), fontsize=20, color="white", weight="bold") #annotate each agent with how many sheep each wolf has eaten
    
    # Stopping Conditions
    # Sum all values in environment, when less than % of environment defined in variables, stop simulation. End process time and add process time to stopping condition message
    if sum(sum(x) for x in environment) < total*edepleted:
        carry_on = False
        end = time.process_time() 
        print("Stopping condition met - Environment depleted.",  "simulation time = " + str(end - start) + " seconds")
    
    # Return number of items in agent list and stop simulation when all sheep have been eaten. End process time and add process time to stopping condition message
    if len(agents) == 0:
        carry_on = False
        end = time.process_time() 
        print("Stopping condition met - All sheep have been eaten!", "simulation time = " + str(end - start) + " seconds")
    
    ## Write out environment results to text file. This is set to overwrite the textfile everytime the model is run.
    with open('out.txt', 'w', newline='') as f:     
        env_writer = csv.writer(f)     
        for row in environment:         
            env_writer.writerow(row)

#Define the carry on
carry_on = True

## animation is looped until carry_on is met
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
    
## Define function that will initiate the model
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function)
    canvas.draw()
 
## GUI settings / design   
window = tkinter.Tk()
window.title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=window)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) #link command 'run' to run model function
window.mainloop()