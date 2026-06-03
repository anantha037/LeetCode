class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(nums,target,l,r):
            if l>=r:
                return -1
            mid = (r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return binary_search(nums,target,l,mid)
            else:
                return binary_search(nums,target,mid+1,r)
        
        res = -1
        n = len(matrix[0])

        for i in matrix:
            
            res = max(res,binary_search(i,target,0,n))
        
        return True if res >=0 else False
