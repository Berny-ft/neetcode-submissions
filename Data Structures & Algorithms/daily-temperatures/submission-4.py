class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ''' 
        you need stacik
        you pushp teh stack the current value as well as its index

        when you get to a new avlaue you chekc the stack if there is a vlue smaller than it 
        at the index ov that value in teh sack you replace in the solutions array the value by the differnece in idices 

        sudocode
        stck 

        sol = [0] * n

        for i in temps:
            while stack and top of stack smaller than this 
                change value at indice of value on top of stack by current index - top stack index
            
            push this value onto stack (value, index)

        # the last value will remain 0
        retuurn the sol array 

        '''
        stack = []
        sol = [0] * len(temperatures)

        for i,val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                indice = stack[-1][1]
                value = i - (stack[-1][1])

                sol[indice] = value
                stack.pop()

            stack.append( (val,i) )

        
        return sol

        