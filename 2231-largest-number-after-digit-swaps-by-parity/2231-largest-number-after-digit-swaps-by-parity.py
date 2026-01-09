class Solution:
    def largestInteger(self, num: int) -> int:
        check = int(str(num)[0])

        first = []
        second = []

        for i in str(num):
            if int(i)%2==0:
                first.append(i)
            else:
                second.append(i)
        first.sort(reverse=True)
        second.sort(reverse=True)
    
        res = ''
        if check%2!=0:
            first,second = second,first
        
        if len(first)<len(second):
            n='second'
        else:
            n = 'first'
        
        for i, j in zip(first,second):
            res+=i+j
        if n  == 'first':
            val = ''.join(first[len(second):])
        else:
            val = ''.join(second[len(first):])

        return int(res+val)
        