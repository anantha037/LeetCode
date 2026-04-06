class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = -1
        left = 0 
        right = len(letters)-1

        while left<=right:
            mid = (left+right)//2

            if letters[mid]==target:
                left = mid+1
            elif letters[mid]<target:
                left = mid+1
            else:
                res = letters[mid]
                right = mid-1

        if res!=-1:
            return res
        else:
            return letters[0]
    

                

