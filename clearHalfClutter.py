
# 1. identify what smallest set will remove half the integers in an array
# 2. first sort this array, so you know, then split it half. find out which 
# 3. 

# 2 <= arr.length <= 105
# arr.length is even.
# 1 <= arr[i] <= 105
from collections import Counter
from itertools import accumulate

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        return next(i+1 for i,n in enumerate(accumulate(reversed(sorted(Counter(arr).values())))) if n >= len(arr)//2)


def testSolution(arr: list[int], expected: int) -> bool:
    s = Solution()
    assert expected == s.minSetSize(arr)

testSolution([3,3,3,3,5,5,5,2,2,7], 2)
testSolution([1,9], 1)
testSolution([3,3,3,3,3,3,3,3,3,5,5,5,5,2,2,7], 1)