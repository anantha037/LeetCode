class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        res = 0
        time_taken = []

        paired_and_sorted = sorted(zip(position, speed))
        position, speed = map(list, zip(*paired_and_sorted))
        print(position, speed)


        for i in range(len(position)):
            pos = position[i]
            s = speed[i]
            time_taken.append((target-pos)/s)
        
        
        stack = []
        
        for i in range(len(position)-1,-1,-1):
            if stack and stack[-1]>=time_taken[i]:
                continue
        
            stack.append(time_taken[i])
    
        return len(stack)


                
                
