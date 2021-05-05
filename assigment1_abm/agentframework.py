#agentframework
import random

class Agent:
    # Agent constructor
    def __init__ (self, environment, agents, y=None, x=None):

        self.environment = environment #used as food for agents to eat in def eat
        self.store = 0                 #creates the food stores for the agents to use in def eat
        self.agents = agents           #used for the sharing_with_neighbour function 
        self.record = 0                #create record for how many times an agent is sick
        self.count = 0                 #create count for how many times an agent moves
        
        # DOES NOT WORK AS INTENDED. If the number of agents specified in the variables exceeds the number of td_ys/td_xs pairs, 
        # the code will complain that the 'list index is out of range'
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        
        
    def move(self):  # rules for moving
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300 #if random number is <0.05, add 1 to the y-axis of the agent
            self.count += 1             #counts how many times the agent has moved
        else:
            self.y = (self.y - 1) % 300 #if random number is >0.05, add 1 to the y-axis of the agent
            self.count += 1             #counts how many times the agent has moved

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300 #if random number is <0.05, add 1 to the x-axis of the agent
        else:
            self.x = (self.x - 1) % 300 #if random number is >0.05, add 1 to the x-axis of the agent

    def __repr__(self):
        return "%s, is at coordinates x:%s y:%s, has a store of %s, and has been sick %s time/times"  % (self.count, self.x, self.y, self.store, self.record)
    
    def __str__(self):
        return "%s, is at coordinates x: %s, y: %s, has a store of %s, and has been sick %s time/times" % (self.count, self.x, self.y, self.store, self.record)

    
    def eat(self): # rules for eating
        if self.environment[self.y][self.x] > 100:    #if the environment has more than 100
            self.environment[self.y][self.x] -= 100   #take 100 from the environment
            self.store += 100                         #add 100 to agent store
        else:
            self.store += self.environment[self.y][self.x]  #if the agents store is equal to environment
            self.environment[self.y][self.x] = 0            #set environment to 0
        
        if self.store >= 1000:                         #if the stores are more than or equal to 1000
            self.environment[self.y][self.x] += 100    #add 100 back to the environment
            self.record += 1						   #add 1 to record everytime an agent is sick
            self.store = 0                             #reset the agent store back to 0
 
    #calculate the distance between agents using pythagoras
    def distance_between(self, agent):
        return ((self.x - agent.x)**2 + (self.y - agent.y)**2)**0.5
     
    #share resources with other agents	 
    def share_with_neighbours(self, neighbourhood, agents):
            for agent in self.agents:
                 dist = self.distance_between(agent)
                 rdist = round(dist,2)          #round distance to 2 decimals - easier to read when reported
            if dist <= neighbourhood:           #if the distance between self and agents is less than the neighbourhood defined in the model;
                sum = self.store + agent.store  #add the two agent's stores together
                ave = round(sum/ 2)             #divide and average the stores. Round used so no decimal places occur in the animation
                self.store = ave                #agents have the same averaged food stores
                agent.store = ave 
                # print what amount was shared and at what distance everytime this occurs
                print("Agent after move " + str(agent) + " and is sharing " + str(ave) + " from a distance of " + str(rdist))
    
class  Wolf:
	#wolf constructor
    def __init__(self, environment, neighbourhood):
        self.y = random.randint(0, 99)       #randomly select a starting position from 0-99 for y.axis
        self.x = random.randint(0, 99)       #randomly selects a starting position from 0-99 for x.axis
        self.store = 0                       #creates the food stores for the wolf to use in def eat_agents
        self.count = 0                       #creates the count for the wolf to use in def eat_agents when a sheep is eaten.
                                             #Also used when annotating the model display how many sheep each wolf has eaten.
                    
            
    def move(self):
    # wolves move up to 3 places per iteration
        if random.random() < 0.5:
            self.x = (self.x + 3) % 300  #if random number is <0.05, add 3 to the x-axis of the agent
        else:
            self.x = (self.x - 3) % 300  #if random number is >0.05, add 3 to the x-axis of the agent

        if random.random() < 0.5:
            self.y = (self.y + 3) % 300  #if random number is <0.05, add 3 to the y-axis of the agent
        else:
            self.y = (self.y - 3) % 300  #if random number is >0.05, add 3 to the y-axis of the agent
        
    ##calculate distance between wolf and agents        
    def distance_between(self, agents):
        return (((self.x - agents.x) **2) + ((self.y - agents.y)
                 **2))**0.5    
 
    def eat_agents(self, neighbourhood, wolves, agents):
        for wolf in wolves:
            for agent in agents:
                dist = self.distance_between(agent) 
                if dist <= neighbourhood:
                    # wolf kills the agent and takes the store. Also records each time this action happens with count.
                    self.store += agent.store
                    self.count += 1
                    ## Remove agent from list
                    agents.remove(agent)
    
