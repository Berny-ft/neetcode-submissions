class Solution:
    def rob(self, nums: List[int]) -> int:
        # you do need to go through all the houses
        # got a better ide of the algo rihtm here 
        # so we initiate boths possiblities to 0 
        # now everytime you encounter a house you have the option to either rob it or not 
        # but in reality we aren't actully doing that we are deciding how much much woudl we get total 
        # if we decided to rob it within the rules 
        # therefore you fetch the maximum amount y ou are llowed to posses when reaching that house 
        # it is going to be either rob1 or rob2. rob2 representing the latest house you've robbed 
        # rob1 representing the house right before. because of the rules you have to choose between the two of them 
        # you obviously choose the one that holds the most value. 
        # upon selecting it you set the value of rob2 to that amount plus the current value
        # and you set the value or rob 1 to be the older value of rob2
        # we aren't actully keeping track of all branches. we are just keeping track of the most lucrative one yet
        # rob1 and rob2 just give you the 2 greatest prices you've reached yet  and in the condition 
        #you do rob1+i because rob 2 represents the latest househouse you've robbed so you have to skip it... not sure 
        # this explanation is kind worng 
        rob1,rob2 = 0,0

        for i in nums:
            temp = max(i+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return temp