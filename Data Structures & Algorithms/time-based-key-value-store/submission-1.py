from collections import defaultdict
class TimeMap:

    '''
    you need a dictionary to store the key value pairs

    you also need 
    how do you keep them sroted 
    you could go with a list but accessing an exact time woudld int' make snese : 
    aheap doesn't wokr 
    a binary tree woudl take logn to find teh value and if it doesnte exit we hve to go back ot the aprent and return the paerent but if the arentis to theright ... no that is not it 

    you coudl just keep a list if value and time stapm and od forwad pass..
    actually you coudl just keep alist of tmie tampe and keey appending  and ahve an object attached to each index so that is the same binary serach since it is sorted yep binary search 


    so a dict that stores key and (timestamp,value)
    set you set andapend the value pair 
    get binary sarch if you find the time stampe return its value 
    if you dont' find it return mid - 1 if if greater than 0 
    '''

    def __init__(self):
        self.table = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.table[key]
        res = ""
        left,right= 0, len(pairs) - 1

        while left <= right:
            mid = left + (right-left) //2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res

        
