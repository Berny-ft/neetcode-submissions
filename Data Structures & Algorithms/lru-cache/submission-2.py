from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity 
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # move to from 
            self.cache.move_to_end(key,last=False)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key,last=False)
            self.cache[key] = value

        else:
            self.cache[key] = value
            self.cache.move_to_end(key,last=False)
            if len(self.cache) > self.capacity:
                self.cache.popitem()
        
        
