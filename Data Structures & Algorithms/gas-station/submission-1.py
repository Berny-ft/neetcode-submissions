class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        volume = 0
        start = 0
        n = len(gas)

        for i in range(n):
            volume += gas[i] - cost[i]
            if volume  < 0: # failing so this is the new start
                start = i+1
                volume = 0
        
        return start
                

