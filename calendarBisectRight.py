# constraints
# 0 <= start < end <= 109
# At most 1000 calls will be made to book.
from sortedcontainers import SortedList

class MyCalendar:
    bookings = None

    def __init__(self):
        self.bookings = SortedList()
        
    def book(self, start:int, end:int) -> bool:
        if len(self.bookings) <= 0:
            self.bookings.add((start,end))
            return True
        idx = self.bookings.bisect_right((start, end))
        if idx > 0:
            self.bookings.add((start,end))
            print(self.bookings)
            return True
        else:
            return False


def runCalendarTest(input: list[int], expected: list[bool]) -> bool:
    obj = MyCalendar()
    results = []
    for i in input:
        results.append(obj.book(*i))
    
    print(results, expected, results == expected)


runCalendarTest(
    [[37,50],[33,50],[4,17],[35,48],[8,25]],
    [True,False,True,False,False],
)
runCalendarTest(
    [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]],
    [True, True, False, False, True, False,True, True, True, False],
)
