class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        sorted_data = sorted(tasks, key=lambda x: abs(x[0] - x[1]),reverse=True)
        
        answer = [sorted_data[0][0],sorted_data[0][1]]

        for i in range(1, len(sorted_data)):
            check = answer[1]-answer[0]
            if check<sorted_data[i][1]:
                diff = sorted_data[i][1]-check
                answer[1] += diff
            answer[0] += sorted_data[i][0]

        return answer[1]