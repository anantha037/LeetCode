class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []


        for asteroid in asteroids:
            negative = True if asteroid<0 else False

            if negative and answer:
                while answer and answer[-1]>0 and abs(asteroid)>answer[-1]:
                    answer.pop()
                if answer:
                    if answer[-1]==abs(asteroid):
                        answer.pop()
                        continue
                    elif answer[-1]>0:
                        continue
         
            answer.append(asteroid)
   
        return answer