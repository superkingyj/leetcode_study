from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.calendar = SortedDict()
        

    def book(self, start_time: int, end_time: int) -> int:
        cnt = 0
        max_cnt = 0
        
        self.calendar[start_time] = self.calendar.get(start_time, 0) + 1
        self.calendar[end_time] = self.calendar.get(end_time, 0) -1
        
        for time in self.calendar:
            cnt += self.calendar[time]
            max_cnt = max(cnt, max_cnt)
        
        return max_cnt
            
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)