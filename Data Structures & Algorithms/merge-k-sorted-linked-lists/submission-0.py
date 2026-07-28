# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # so you create a new liked list  or you pick one with the smallest value as your staring one 
        # then you check the eyad of all the ones that remain if they have the same value you are have currently you pop them all 
        # if they don't you increment the value by one and you do it again ? 
        # if there are gaps you do useless computations 
        # a for loop per list then you find the list with the smalest value then you do a for loop for that value and so on 
        # staring fresh removes the complexity of having to insert 

        n = ListNode(-float("inf"))
        curr = n
        while lists:
            # edge case is what if a node is None it hs teo be removed from teh list 
            for i in lists:
                if i is None:
                    lists.remove(i)
            if not lists:
                break

            m = lists[0]
            index = 0
            for i,v in enumerate(lists):
                if v.val < m.val:
                    m = v
                    index = i
            

                
            curr.next = ListNode(m.val)
            curr = curr.next

            # remove the taken node 
            lists[index] = lists[index].next
        
        return n.next
            

        