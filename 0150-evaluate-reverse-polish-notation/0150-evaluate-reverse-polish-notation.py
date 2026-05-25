class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                val2 = stack.pop()
                val1 = stack.pop()

                if i=='+':
                    val = val1+val2
                elif i=='-':
                    val = val1-val2
                elif i =='*':
                    val = val1*val2
                else:
                    val = int(val1/val2)
                
                stack.append(val)
            else:
                stack.append(int(i))

        return stack[0]
