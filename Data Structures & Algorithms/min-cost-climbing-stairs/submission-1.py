class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # so the idea in this position is that you are actually looking for the lowest 
        # cost so this adds onto the noormal climbing stairs because you are optimizing for one of your two optionseach time
        # and you can't always go for the closest step since that might make you more steps 
        # you can't also always take the furthest step since you might end up paying too much evn tho you got therefore
        #[1,2,3,0]
        # wwe append the 0 the end because on the first itration we llok that from teh second to last operation 
        # it is acatuly less expensive to just get to the end with 2 then to get to three then get to 0 
        # because we are actually choosing to pay 2 instead of 23
        cost.append(0)



        for i in range(len(cost)-3, -1,-1):
            # so for the current position I must choose what is the least costtly option i got either one or two
            # the += si because teh current node already has a cost associated. thefore it must be taken into account
            # before actually skipiping to the next number since we woudl just carry the least expensive cost from teh end to the start
            cost[i] += min(cost[i+2],cost[i+1])
        
        return min(cost[0],cost[1])


        