class Solution:
    def smallestPalindrome(self, s: str) -> str:
        obj = Counter(sorted(s))
        res = ''
        mid = ''
        for i in obj:
            if obj[i]%2!=0:
                mid=i
            res+=(i)*(obj[i]//2)
        
        return res+mid+res[::-1] if res else mid
        