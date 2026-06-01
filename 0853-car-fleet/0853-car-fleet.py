class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        res = 0
        time_taken = []

        paired_and_sorted = sorted(zip(position, speed))
        position, speed = map(list, zip(*paired_and_sorted))

        stack = []
        for i in range(len(position)-1,-1,-1):
            pos = position[i]
            s = speed[i]
            time_taken = (target-pos)/s

            if stack and stack[-1]>=time_taken:
                continue
            stack.append(time_taken)
    
        return len(stack)


                
                
