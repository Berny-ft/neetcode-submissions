class Solution:
    def isValid(self, s: str) -> bool:
        ''''

        push close of open 
        if closes pop from stack if it matchies continue, if it doesnt return false
        if at the end the stack isn't empty return false

        '''

        stack = []
        m = {
            "{":"}",
            "[":"]",
            "(":")",
        }
        for i in s:
            if i in m:
                stack.append(m[i])
            else:
                if not stack:
                    return False
                close = stack.pop()
                if i != close:
                    return False
        
        if stack:
            return False
        return True
        