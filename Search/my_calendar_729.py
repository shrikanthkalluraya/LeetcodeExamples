# 729. My Calendar Iclass MyCalendar:
'''
vYou are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
'''

    def __init__(self):
        self.calendar = []

    def book(self, startTime: int, endTime: int) -> bool:
        left, right, idx = 0, len(self.calendar)-1, len(self.calendar)
        while left < right:
            mid = (left + right) // 2
            if self.calendar[mid][0] < startTime:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        if (idx > 0 and self.calendar[idx-1][1] > startTime) or (idx < len(self.calendar) - 1 and self.calendar[idx+1][0] < end_time):
            return False
        self.calendar.insert(idx, (startTime, endTime))
        return True
 
