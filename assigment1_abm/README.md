# AGENT BASED MODEL

This repository is made for assignment 1 of the GEOG5990M module for the University of Leeds. The ABM was created in python and simulates sheep and wolves in a field.

To use this code, all files within the repository must be downloaded.

These are:
* model.py (base model)
* agentframework.py (defines the class Agent and Wolf for the model)
* in.txt (contains the environment data)

## The Model

The ABM simulates the randomised movement of sheep in a field. As they move they eat data and remove the data from the environment. When they eat too much they will be sick and deposit some data back into the environment. Wolves can also be added to the model. The wolves will move across the environment and eat the sheep and any data they store when within a set distance (defined by the neighbourhood variable).

Within the model, the following variables can be altered:
* num_of_agents (define how many sheep in the model)
* num_of_wolves (define how many wolves in the model)
* num_of_iterations (how often frames are shown in the GUI animation)
* neighbourhood (how close the sheep must be to share resources, also how close wolves must be to sheep to eat them)
* percentenvironmentdepleted (Define the % the environment should be depleted by to enable stopping condition)

The agents and wolves are displayed as diamonds in the model, white for sheep and black for wolves. The agents are annotated with how many times they have been sick. The wolves are annotated with how many sheep they have eaten.

The model has two stopping conditions. The first stopping condition occurs when the agents (sheep) deplete the environment by the user specified amount. The second stopping condition occurs when all the sheep are eaten by the wolves.

## Known Issues

The model imports the starting x and y for each agent from the web. When the number of agents specified is greater than the number of x/y pairs retrieved from the web, the model will fail as it does not know what to do with the extra agents. An attempt was made to apply a random x and y to any extra agents in line 15 - 22 in the agentframework, but this does not currently work.

When the agents / wolves exit the boundary of the model, they will appear at the opposite side. They do not turn back when they hit the model domain. 

## Further Ideas

The speed of the agents or wolves could be varied depending on how much they have in their store.

Agents could be asssigned a gender and could reproduce when in close proximity to each other over an extended period of time.

Wolves could die of starvation if they do not eat sheep within a time period.

Add boundary conditions to model so agents / wolves must turn back on themselves if they reach the domain edge.