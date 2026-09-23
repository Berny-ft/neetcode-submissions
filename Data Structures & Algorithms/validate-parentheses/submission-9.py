class Solution:
    def isValid(self, s: str) -> bool:
        # push the oppsoite tothe satck of the it is opene
        '''
        if you see an opening ou push a claosed 
        if you meet a closed check if the pop stack valie is a match if not retunr false
        if at teh end the stack is not emppth retunr false 

        else return true:


        ''' 
        stack = []
        m = {
            '(': ')', '{':'}', '[':']'

        }
        for i in s:
            if i in m:
                stack.append(m[i])
            else:
                if not stack:
                    return False
                value = stack.pop()
                if i != value:
                    return False
        
        if stack:
            return False

        return True
        