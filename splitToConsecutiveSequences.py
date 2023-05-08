# Contributed by: Bryan Ling


# You are given an integer array nums that is sorted in non-decreasing order.

# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.

# A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

# Example 1:

# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
# Example 2:

# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
# Example 3:

# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

# Constraints:

# 1 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
# nums is sorted in non-decreasing order.

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        
        spacing = 0
        return self.isPossibleHelper(nums, 0)
        
        # recurse through the list
        # if you encounter a sequence, start looking for it
        # each time you encounter a number not in the expected sequence, spawn a new sequence finder
        # if at any point there's a sequence that ends without an option (the next number is 1+ the expected number to continue the sequence) and the sequence is not yet 3, then return false
    def isPossibleHelper(self, nums: list[int], spacing: int) -> bool:
        seq = []
        in_seq = False
        idx = 0
        while idx < len(nums):
            # new seq
            if not in_seq:
                in_seq = True
                seq.append(nums[idx])
            # the num in seq did not increment
            elif nums[idx] == seq[-1]:
                return self.isPossibleHelper(nums[idx:], spacing + 1)
            # number in seq incremented as expected
            elif nums[idx] == seq[-1] + 1:
                seq.append(nums[idx])
            # the num in seq did more than increment, this seq is done, but is it 3?
            elif nums[idx] > seq[-1] + 1:
                if len(seq) < 3:
                    return False
                else:
                    # this seq is done, keep going
                    return self.isPossibleHelper(nums[idx:], spacing + 1)

            idx += 1
        
        # if the list is complete, but the sequence is not 3, return False, otherwise return True
        return len(seq) >= 3
        
        
def testSolution(arr: list[int], expected: int) -> bool:
    s = Solution()
    res = s.isPossible(arr)
    print(res)
    assert expected == res

testSolution([3,3,3,3,5,5,5,2,2,7], False)
testSolution([1,9], False)
testSolution([3,3,3,3,3,3,3,3,3,5,5,5,5,2,2,7], False)
testSolution([1,2,3,4,5,6], True)
testSolution([1,2,3,3,4,5], True)
testSolution([1,2,3,3,4,4,5,5], True)
