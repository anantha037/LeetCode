class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        hour_angle = (hour%12)*30
        minute_angle = minutes*5.5

        
        total_angle = hour_angle-minute_angle

        return abs(total_angle) if abs(total_angle)<180 else 360-abs(total_angle)