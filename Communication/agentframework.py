#agentframework
import random

class Agent():
    
    def __init__ (self, environment, agents):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
    def move(self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        
    def __repr__(self):
        return "<Agent x:%s y:%s store = %s>"  % (self._x, self._y, self.store)
    
    def __str__(self):
        return "x: %s, y: %s, store = %s" % (self._x, self._y, self.store)

    
    def eat(self): # can you make it eat what is left?
        if self.environment[self._y][self._x] >= 100:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
    #def eatall(self):
        #value = self.environment[self._y][self._x]
        #if self.environment[self._y][self._x] <= 300:
            #self.store += self.environment[self._y][self._x]
            #self.environment[self._y][self._x] - value
            
    def drop(self): 
       if self.store >=150:
           self.environment[self._y][self._x] += 150
           self.store -= 150
            
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
                        print("Agent at " + str(agent) + " is sharing " + str(dist) + " " + str(ave))
                        
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
