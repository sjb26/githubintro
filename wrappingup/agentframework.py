#agentframework
import random

class Agent:
    
    def __init__ (self, environment, agents, y=None, x=None):

        self.environment = environment
        self.store = 0
        self.agents = agents
        self.record = 0
        self.count = 0
        
        if (y == None):
            self.y = random.randint(0,99)
        else:
            self.y = y
        if (x == None):
            self.x = random.randint(0,99)
        else:
            self.x = x
        
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
            self.count += 1
        else:
            self.y = (self.y - 1) % 100
            self.count += 1

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
        
    def __repr__(self):
        return "%s, is at coordinates x:%s y:%s, has a store of %s, and has been sick %s time/times"  % (self.count, self.x, self.y, self.store, self.record)
    
    def __str__(self):
        return "%s, is at coordinates x: %s, y: %s, has a store of %s, and has been sick %s time/times" % (self.count, self.x, self.y, self.store, self.record)

    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 100:
            self.environment[self.y][self.x] -= 100
            self.store += 100
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0 
        
        if self.store > 1000:
            self.environment[self.y][self.x] += 100
            self.record += 1
            self.store = 0
           
    def distance_between(self, agent):
        return ((self.x - agent.x)**2 + (self.y - agent.y)**2)**0.5
            
    def share_with_neighbours(self, neighbourhood, agents):
            for agent in self.agents:
                 dist = self.distance_between(agent)
                 rdist = round(dist,2)
            if dist <= neighbourhood:           #if the distance between self and agents is less than the neighbourhood defined in the model;
                sum = self.store + agent.store  #add the two agent's stores together
                ave = round(sum/ 2)             #divide and average the stores. Round used so no decimal places occur in the animation
                self.store = ave                #agents have the same averaged food stores
                agent.store = ave 
                print("Agent after move " + str(agent) + " and is sharing " + str(ave) + " from a distance of " + str(rdist))
    
class  Wolf:
    def __init__(self, environment, neighbourhood):
        self.environment = environment    
        self.y = random.randint(0, 99)   
        self.x = random.randint(0, 99)
        self.neighbourhood = neighbourhood
        self.store = 0
        self.count = 0
            
    def move(self):
    # wolves move up to 3 places per iteration
        if random.random() < 0.5:
            self.x = (self.x + 3) % 100
        else:
            self.x = (self.x - 3) % 100

        if random.random() < 0.5:
            self.y = (self.y + 3) % 100
        else:
            self.y = (self.y - 3) % 100
            
    ##calculate distance            
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
                    ## Remove agent
                    agents.remove(agent)
    
