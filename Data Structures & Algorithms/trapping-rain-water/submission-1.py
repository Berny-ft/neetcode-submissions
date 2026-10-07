class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        total amount of water between the bars 
        so many lakes we cinpute thevolume of water within eahc lake we add them all up 

        so starting from the left i have a colun  that represnets the mount of height i can get moving to the right so have have potenvolu that i can hold based on that heigh  that amount of water has a maximum height of height[i] so i then move to the right if the next column is less than high at prev the differnce in high is the amount of water than can be coumulated  so max thus far - 


        '''

        '''
        sudocode
        keep a left 
        keep a right 
        keep max left keep max right 
        watervolme

        whle left is left is less than right 
            check which side has min high 
                if th current high is treager than the preivous max heihgt
                    update the max high 
                else:
                    water volume += maxhieght- height
                    
                incremnt taht side 
        
        return water volume


        '''
        water = 0
        left_max = 0
        right_max = 0
        left = 0
        right = len(height)-1

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    # grab the water volume 
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water




