class Solution:
    def isValid(self, s: str) -> bool:
        # this is a stack problem 
        # here's the stargegy for every open bracket you store a closed on in your stack the closed must match the type of that opened. then when you encounter a closed it must match the top of the stack if so pop the stack and move on if it does not error failure. after having gone thorugh the entire string your stack must be empty signaling that in addition of through through all parenthesis you also closed all open brackets

        

        h = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        stack = []


        for val in s:
            if val in h:
                stack.append(h[val])
            elif stack and stack[-1] == val:
                stack.pop()
            else:
                # if stack[-1] is not elqual to val or there is not stack 
                return False
        
        if not stack:
            return True
        else:
            return False
        