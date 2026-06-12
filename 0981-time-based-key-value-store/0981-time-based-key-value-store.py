class TimeMap:

    def __init__(self):
        self.obj = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.obj[key].append([timestamp,value])
        return None

    def get(self, key: str, timestamp: int) -> str:
        if not self.obj[key]:
            return ''
        arr = self.obj[key]
        if timestamp<arr[0][0]:
            return ''
        
        l = 0
        r = len(arr)-1

        while l<=r:
            mid = (r+l)//2

            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                l = mid+1
            else:
                r = mid-1
        
        return arr[l-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)