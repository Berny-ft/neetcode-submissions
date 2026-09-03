class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the idea is that we are looking for a pair of indices 
        # representing two elements of our numbers array such that if they are aadded 
        # together they will be equal to a target number 

        # the approach to use to to do a single pass 
        # if you encounter an element you check in hour hasmap if you have an element that complements it to get the target. 
        # if there is none you store the element and ist indice in teh hasmap
        # there is  alawys a solution so no edgecase there

        h = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in h:
                return [h[target-val],i]
            else:
                h[val] = i
        