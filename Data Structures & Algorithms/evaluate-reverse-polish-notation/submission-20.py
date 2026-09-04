class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stoare a stack

        # store a current value 

        # while tokens stack values 

        # if value is operand pop the last two values and apply the operand

 

        def comp(stack,c):

            if c =="+":
                a = stack.pop()
                b = stack.pop()
                return a+b
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                return b-a
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
               
                return int(b/a)
            elif c =="*":
                a = stack.pop()
                b = stack.pop()
                return b*a

        ops = ("+","*","-","/")
        stack = []

        for val in tokens:
            if val in ops:
                stack.append(comp(stack, val))
            else :
                stack.append(int(val))

        return stack[0]