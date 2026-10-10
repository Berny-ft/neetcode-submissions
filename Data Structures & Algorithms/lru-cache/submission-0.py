from collections import OrderedDict

"""
use an ordered dic tso that the ordering is done by itself

for get 
you just make sure to move to front if the key exist 
and return the value 


for put

you check if key's areyd tehre 
you move it to front 

you then update teh value 

"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1

        self.cache.move_to_end(key,last=False) # 
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key,last=False)
            self.cache[key] = value
            return
        else:
            if len(self.cache) == self.capacity and key not in self.cache:
                self.cache.popitem()

            self.cache[key] = value
            self.cache.move_to_end(key,last=False)
        
        


        
