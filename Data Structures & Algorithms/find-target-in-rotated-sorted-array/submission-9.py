class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ''' so the idea is that there is always a side that is sorted and that allows us to look at that side and determine if the target is within. if itsi not we know that the target is going ot be on the other side so we change the left and right targetters aso then we know which side is the the target is that allows us to still have binary search because oen side will tell us sitll of hte target is in one side or the other
        
        
        
        we keep the left and right 
        we have the while loop ocndition htat is relevant for binary serach 

        if the number at mid is thetaret we return the mid 
        if not we determine which is side side the target is on and we use that side to chekc if we get oout of hte while loop we return -1
        '''

        ''
        left = 0
        right = len(nums)-1

        while left <= right : 
            mid = left + (right-left) //2
            if nums[mid] == target:
                return mid

            if  nums[left] <= nums[mid]   : #is left sorted
                if  nums[left] <= target <=  nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            
            else: # teh target is right 
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid -1


        return -1

        ''' i need to think about this a lot mroe than i currenlty am 
        if a side is sorted and the target is within that does that mean? 
        it means taht the right shoudl change to mid-1

        what if the target is not there well it doens't eamn anything so i hav eto go right 
        but on the right sides i know that it is not sorted which doesnt giv eme mroe info bute it just means that i have to peorm the same setps 
        what if left wasn't sorted but still had the target beacuse right didnt have it ? 
        i dont' know why are we looking for the sotrted side 
        the sorted side tells us ??? why do we need storing for binary search ? to tell wich side to go afeer guessing the middle. ok so here why woudl we need to check which side is sorted . again to tell us whic  ide we sshoudl look into 

        so left is sorted and rightis not 
        we knwo that left is the sorted side 
        say righ tis sorrted we know that right is the shorted side 

        cool so then what know which side is sorted allows us to knwo if that side has the target by induction of the sorreed nature  so because we are able to tell which isde has the sohas the target we can go in that side so having one side sorted still allows us to do binary search. 

        therefore what do we do ? 
        well you must check left and if left is sorted if both are correct we go left 
        else we go right 

        now you are in the righ t: 
        say right is sorted but not correct you must go left 

        ooh so sorted is the first condition 
        then containingis the target sorted allows us to know which side has the information that is usable and then the target beign within is the condition that allows us to tell which side we want to choose 

        so the algo goes this way 
        is left sorted:
            is target in left:
                go left 
            else
                go right
        righ tis sorted 
            is target on the righ t
                go righ t
            else 
                go left

        '''







