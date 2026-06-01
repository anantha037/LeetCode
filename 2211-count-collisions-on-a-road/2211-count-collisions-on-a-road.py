class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []

        answer = 0

        for car in directions:
            if car =='L':
                if stack and stack[-1]!=car:
                    if stack[-1]=='S':
                        answer +=1
                        continue
                    else:
                        answer +=2
                        stack.pop()
                        while stack and stack[-1]=='R':
                            stack.pop()
                            answer +=1
                        stack.append('S')
    
                if not stack or stack[-1]=='S':
                    continue
            elif car == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    answer +=1
            
            stack.append(car)
        return answer
