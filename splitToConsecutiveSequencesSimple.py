# Contributed by: Bryan Ling

from collections import deque
 
class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        ## seqs = [[expectedNum, length], [expectedNum, length], [expectedNum, length], ...]
        seqs = deque()
        
        for n in nums:
            found = False
            for s in seqs:
                # is this num n of an existing seq?
                if s[0] == n:
                    found = True
                    s[0] = n + 1 # add the next expected num in
                    s[1] += 1
                    print(s)
                    break
            
            # num n didn't fit anywhere, why?
            if not found:
                seqs.appendleft([n + 1, 1])


        for s in seqs:
            if s[1] < 3:
                return False

        return True

True

    
def testSolution(arr: list[int], expected: int) -> bool:
    s = Solution()
    res = s.isPossible(arr)
    print(res)
    assert expected == res

testSolution([3,3,3,3,5,5,5,2,2,7], False)
testSolution([1,9], False)
testSolution([3,3,3,3,3,3,3,3,3,5,5,5,5,2,2,7], False)
testSolution([1,2,3,4,5,6], True)
testSolution([1,2,3,3,4,5], True) # 1,2,3, 3,4,5
testSolution([1,2,3,3,4,4,5], True) # 1,2,3,4, 3,4,5
testSolution([1,2,3,3,3,4,4,4,5,5,6], True) # 1,2,3,4, 3,4,5, 3,4,5,6

# testSolution([1,2,3,3,4,4,5,5], True)
# testSolution([1,2,3,4,4,5], False)
