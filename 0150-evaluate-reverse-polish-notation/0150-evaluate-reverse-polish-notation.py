class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = "+-*/"

        for i in tokens:
            if i in operators:
                val2 = stack.pop()
                val1 = stack.pop()

                if i=='+':
                    val = val1+val2
                elif i=='-':
                    val = val1-val2
                elif i =='*':
                    val = val1*val2
                else:
                    val = val1/val2
                
                stack.append(int(val))
            else:
                stack.append(int(i))

        return stack.pop()
