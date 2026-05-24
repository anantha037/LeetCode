class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
            
        output = []

        queue = deque()
        
        l = 0
        r = 0
        n = len(nums)
        
        while r<n:
            if not queue or queue[-1]>=nums[r]:
                queue.append(nums[r])
            elif queue[-1]<nums[r]:
                while queue and queue[-1]<nums[r]:
                    queue.pop()
                queue.append(nums[r])
        
            if r>=k-1:
                output.append(queue[0])
                if queue and queue[0] == nums[l]:
                    queue.popleft()
                l+=1
            r+=1
        
        return output

        
        


        