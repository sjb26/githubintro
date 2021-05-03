#agentframework
import random

class Agent():
    def __init__ (self):
        self._y = random.randint(0,99)
        self._x = random.randint(0,99)
        
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
        return "<Agent y:%s x:%s>"  % (self._y, self._x)
    
    def __str__(self):
        return "From str method of Test: y is %s, x is %s" % (self._y, self._x)
        
    
                
    