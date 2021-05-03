#agentframework
import random

class Agent():
    
    def __init__ (self, environment, agents, y, x):
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.record = 0
        self.count = 0
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
            self.count += 1
        else:
            self._y = (self._y - 1) % 100
            self.count += 1

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    
    ##def speed(self):
        ##if self.store <= 50:  
           ## self._y (self._y + 3) % 100
       ## else:
            ##self._y (self._y + 1) % 100
        ##if self.store <= 50:  
            ##self._x (self._x + 3) % 100
        ##else:
           ## self._x (self._x + 1) % 100
            
        
    def __repr__(self):
        return "%s, is at coordinates x:%s y:%s, has a store of %s, and has been sick %s time/times"  % (self.count, self._x, self._y, self.store, self.record)
    
    def __str__(self):
        return "%s, is at coordinates x: %s, y: %s, has a store of %s, and has been sick %s time/times" % (self.count, self._x, self._y, self.store, self.record)

    
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
            
    #def eatall(self):
        #value = self.environment[self._y][self._x]
        #if self.environment[self._y][self._x] <= 300:
            #self.store += self.environment[self._y][self._x]
            #self.environment[self._y][self._x] - value
            
    def drop(self): 
       if self.store >=100:
           self.environment[self._y][self._x] += 100
           self.store -= 100
           self.record += 1
            
    def share_with_neighbours(self, neighbourhood):
            #print(neighbourhood)
            for agent in self.agents:
                # Don't share with self for speed (not that it matters much)
                if(self != agent):
                    #calculate the distance between self and the current other agent
                    dist = self.distance_between(agent) 
                    #if distance is less than or equal to the neighbourhood
                    if dist <= neighbourhood:
                        sum = self.store + agent.store
                        ave = sum /2
                        self.store = ave
                        agent.store = ave
                        print("Agent after move " + str(agent) + " and is sharing " + str(ave) + " from a distance of " + str(dist))
        
                        
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
